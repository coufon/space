# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Iterable

import pyarrow as pa
import ray

from space.core.utils.uuids import random_id
from space import Dataset, RayOptions


def test_write_ray_to_space(tmp_path):
  schema = pa.schema([
      pa.field("int64", pa.int64()),
      pa.field("float64", pa.float64()),
      pa.field("binary", pa.binary())
  ])
  ds = Dataset.create(str(tmp_path / f"dataset_{random_id()}"),
                      schema,
                      primary_keys=["int64"],
                      record_fields=["binary"])

  ray_ds = ray.data.from_arrow(
      [generate_data(range(100)),
       generate_data(range(100, 200))])
  ds.ray(RayOptions(max_parallelism=1)).append_ray(ray_ds)

  print(ds.local().read_all())
  assert False


def generate_data(values: Iterable[int]) -> pa.Table:
  return pa.Table.from_pydict({
      "int64": values,
      "float64": [v / 10 for v in values],
      "binary": [f"b{v}".encode("utf-8") for v in values]
  })
