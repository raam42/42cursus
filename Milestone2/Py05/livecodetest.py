class BooleanProcessor(DataProcessor):
    """Specialized processor for boolean data streams."""

    def validate(self, data: typing.Any) -> bool:
        def is_bool(item: typing.Any) -> bool:
            # Strictly checks for booleans
            return isinstance(item, bool)
            
        if is_bool(data):
            return True
        if isinstance(data, list):
            return all(is_bool(item) for item in data)
        return False

    def ingest(self, data: bool | list[bool]) -> None:
        if not self.validate(data):
            raise ValueError("Improper boolean data")
        
        # Unify data into a list for consistent processing
        items = data if isinstance(data, list) else [data]
        
        for item in items:
            self._storage.append((self._rank_counter, str(item)))
            self._rank_counter += 1


#for the Main block

print("Registering Boolean Processor")
    bool_proc = BooleanProcessor()
    stream.register_processor(bool_proc)