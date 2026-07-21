#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    data_stream.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/21 11:25:00 by rodrigoa          #+#    #+#             #
#    Updated: 2026/07/21 11:25:00 by rodrigoa         ###   ########.fr       #
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
    Central dispatcher that dynamically routes heterogeneous data streams
    to registered specialized processors.
    """

    def __init__(self) -> None:
        """Initializes an empty routing pipeline."""
        self.processors: list[DataProcessor] = []

    def register_processor(self, processor: DataProcessor) -> None:
        """Adds a new processor to the dispatcher."""
        self.processors.append(processor)

    def route_data(self, stream: typing.Iterable[typing.Any]) -> None:
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

            # Replicating the exact warning format from the subject
            if not routed:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def display_statistics(self) -> None:
        """
        Prints current ingestion and storage stats
        for all registered processors.
        """
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            # Reformat class name
            # (e.g., 'NumericProcessor' -> 'Numeric Processor')
            name = (
                processor.__class__.__name__.replace("Processor",
                                                     " Processor"))

            # Using the internal trackers established in Exercise 0
            total = processor._rank_counter
            remaining = len(processor._storage)
            print(f"{name}: total {total} items processed,"
                  f"remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.display_statistics()
    print("\nRegistering Numeric Processor\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    # The exact heterogeneous payload from the subject,
    # including the "wil" typo
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.route_data(batch)
    stream.display_statistics()
    print("\nRegistering other data processors")
    print("Send the same batch again")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    stream.route_data(batch)
    stream.display_statistics()
    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    # Consuming the exact amounts silently, as shown in the example
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream.display_statistics()
