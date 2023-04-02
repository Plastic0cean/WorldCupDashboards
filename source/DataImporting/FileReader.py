import csv 

#TODO: possibility to pass other csv module arguments as kwargs
def csv_reader(file, delimiter, encoding: str="utf-8", quotechar: str=None, **kwargs):
    with open(file, encoding=encoding) as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter, quotechar=quotechar, **kwargs)
        for row in reader:
            yield row


class BatchCsvReader:

    def __init__(self, file: str, delimiter: str, batch_size: int=100_000, encoding: str="utf-8", quotechar: str=None, header: bool=True):
        self.reader = csv_reader(file, delimiter, encoding, quotechar)
        self.header = next(self.reader) if header else None
        self.batch_size = batch_size
    
    def get_batch(self):
        batch = []
        for index, line in enumerate(self.reader):
            if index % self.batch_size==0 and index>0:
                yield batch
                del batch[:]
            batch.append(line)
        yield batch

    def __next__(self):
        batch = self.get_batch().__next__()
        return batch