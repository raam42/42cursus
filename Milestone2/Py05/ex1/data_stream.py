#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    data_stream.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/22 15:41:01 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/22 15:41:01 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import typing
from data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor
)


class DataStream:
    """
    Centtral dispatcher that dynamically routes heterogeneous data streams
    to registered specialized processors.
    """

    def __init__(self) -> None:
        """Initialize an empty routing pipeline."""
        self.processors: list[DataProcessor] = []

    def register_processor(self, processor: DataProcessor) -> None:
        """Adds a new processor to the dispatcher."""
        self.processors.append(processor)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """
        Iterates through incoming data and dynamically routes it to the
        first processor that successfully validates it.
        """
        for item in stream:
            routed = False
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    routed = True
                    break

            if not routed:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        """
        Prints current ingestion and storage stats
        for al registered processors.
        """
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            name = (
                processor.__class__.__name__.replace("Processor",
                                                     " Processor"))

            total = processor._rank_counter
            remaining = len(processor._storage)
            print(f"{name}: total {total} items processed,"
                  f"remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n"
          "\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User Will is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    try:
        stream.process_stream(batch)
    except Exception as e:
        print(f"Failed to process batch of data on stream: {e}")
    stream.print_processors_stats()

    print("\nRegistering other data processors"
          "\nSend the same batch again")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)
    try:
        stream.process_stream(batch)
    except Exception as e:
        print(f"Failed to process batch of data on stream a 2nd time: {e}")
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    try:
        for _ in range(3):
            num_proc.output()
        for _ in range(2):
            text_proc.output()
        for _ in range(1):
            log_proc.output()
        stream.print_processors_stats()
    except Exception as e:
        print(f"{e}")
