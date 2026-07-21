#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    data_processor.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/21 10:21:28 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/21 10:21:28 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import abc
import typing


class DataProcessor(abc.ABC):
    """
    Abstract base class for all data stream processors.
    Enforces a strict contract for validation and ingestion,
    and provides a universal output mechanism.
    """

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        """Evaluates if data type is appropriate for the processor."""
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        """Processes and stores valid data. Raises Exception if invalid."""
        pass

    def output(self) -> tuple[int, str]:
        """Extracts and removes the oldest piece of internally stored data."""
        if not self._storage:
            raise RuntimeError("Storage is empty.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    """Specialized processor for numeric data streams."""

    def validate(self, data: typing.Any) -> bool:
        def is_num(item: typing.Any) -> bool:
            return (isinstance(item, (int, float)) and not
                    isinstance(item, bool))
        if is_num(data):
            return True
        if isinstance(data, list):
            return all(is_num(item) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank_counter, str(item)))
            self._rank_counter += 1


class TextProcessor(DataProcessor):
    """Specialized processor for text data streams."""

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank_counter, item))
            self._rank_counter += 1


class LogProcessor(DataProcessor):
    """Specialized processor for log data streams."""

    def validate(self, data: typing.Any) -> bool:
        def is_valid_log(item: typing.Any) -> bool:
            if not isinstance(item, dict):
                return False
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in item.items()
            )

        if is_valid_log(data):
            return True
        if isinstance(data, list):
            return all(is_valid_log(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            formatted_log = ": ".join(item.values())
            self._storage.append((self._rank_counter, formatted_log))
            self._rank_counter += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    # --- Numeric Processor Testing ---
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # This explicitly passes invalid data to trigger the mypy warning
        num_proc.ingest("foo")  # type: ignore[arg-type]
    except Exception as e:
        print(f"Got exception: {e}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc.ingest(num_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        # Notice the strict newline formatting for numbers
        print(f"Numeric value {rank}: {val}")

    # --- Text Processor Testing ---
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    # --- Log Processor Testing ---
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
