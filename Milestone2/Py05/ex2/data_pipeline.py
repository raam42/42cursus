#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    data_pipeline.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/22 17:06:43 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/22 17:06:43 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import typing
from data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor
)


class ExportPlugin(typing.Protocol):
    """
    Protocol defining the required interfce for export plugins.
    Enforces a strict method signature for duck typing compatibility.
    """
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    """Exports processed data into a manually formatted CSV string."""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [val for _, val in data]
        print(", ".join(values))


class JSONExportPlugin:
    """Exports processed data into a manually formatted JSON string"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("{" + ", ".join(items) + "}")


class DataStream:
    """
    Central dispatcher that dynamically routes data to processors
    and manages export pipelines via plugin integration.
    """
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, processor: DataProcessor) -> None:
        self.processors.append(processor)

    def process_stream(self, stream: list[typing.Any]) -> None:
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
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            name = (
                processor.__class__.__name__.replace("Processor",
                                                     " Processor")
            )
            total = processor._rank_counter
            remaining = len(processor._storage)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Consumes nb elements from all registered data processors,
        and exports them using the provided compatible plugin.
        """
        for processor in self.processors:
            data_to_export = []
            for _ in range(nb):
                try:
                    data_to_export.append(processor.output())
                except RuntimeError:
                    break
            if data_to_export:
                plugin.process_output(data_to_export)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n"
          "\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch1}")
    try:
        stream.process_stream(batch1)
    except Exception as e:
        print(f"Failed to process first batch: {e}")
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    try:
        stream.output_pipeline(3, csv_plugin)
    except Exception as e:
        print(f"Failed to execute CSV output pipeline: {e}")
    stream.print_processors_stats()

    batch2 = [
        21,
        ['I hate AI', 'LLMs are horrible', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"\nSend another batch or data: {batch2}")
    try:
        stream.process_stream(batch2)
    except Exception as e:
        print(f"Failed to process the second batch: {e}")
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    try:
        stream.output_pipeline(5, json_plugin)
    except Exception as e:
        print(f"Failed to execute JSON output pipeline: {e}")
    print()
    stream.print_processors_stats()
