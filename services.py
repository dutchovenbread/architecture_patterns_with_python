from model import OrderLine, Batch
from typing import List

def allocate(line: OrderLine, batches: List[Batch]) -> str:
  batch = next(
    b for b in sorted(batches) if b.can_allocate(line)
  )
  batch.allocate(line)
  return batch.reference
