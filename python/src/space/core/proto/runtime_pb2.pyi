"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2023 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import space.core.proto.metadata_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DataFile(google.protobuf.message.Message):
    """Information of a data file."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    STORAGE_STATISTICS_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Data file path."""
    @property
    def storage_statistics(self) -> space.core.proto.metadata_pb2.StorageStatistics:
        """Storage statistics of data in the file."""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        storage_statistics: space.core.proto.metadata_pb2.StorageStatistics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["storage_statistics", b"storage_statistics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "storage_statistics", b"storage_statistics"]) -> None: ...

global___DataFile = DataFile

@typing_extensions.final
class FileSet(google.protobuf.message.Message):
    """A set of associated data and manifest files."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INDEX_FILES_FIELD_NUMBER: builtins.int
    @property
    def index_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DataFile]:
        """Index data files."""
    def __init__(
        self,
        *,
        index_files: collections.abc.Iterable[global___DataFile] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_files", b"index_files"]) -> None: ...

global___FileSet = FileSet

@typing_extensions.final
class Patch(google.protobuf.message.Message):
    """A patch describing metadata changes to the storage.
    NEXT_ID: 4
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDITION_FIELD_NUMBER: builtins.int
    DELETION_FIELD_NUMBER: builtins.int
    STORAGE_STATISTICS_UPDATE_FIELD_NUMBER: builtins.int
    @property
    def addition(self) -> space.core.proto.metadata_pb2.ManifestFiles:
        """Manifest files to add to the storage."""
    @property
    def deletion(self) -> space.core.proto.metadata_pb2.ManifestFiles:
        """Manifest files to remove from the storage."""
    @property
    def storage_statistics_update(self) -> space.core.proto.metadata_pb2.StorageStatistics:
        """The change of the storage statistics."""
    def __init__(
        self,
        *,
        addition: space.core.proto.metadata_pb2.ManifestFiles | None = ...,
        deletion: space.core.proto.metadata_pb2.ManifestFiles | None = ...,
        storage_statistics_update: space.core.proto.metadata_pb2.StorageStatistics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["addition", b"addition", "deletion", b"deletion", "storage_statistics_update", b"storage_statistics_update"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["addition", b"addition", "deletion", b"deletion", "storage_statistics_update", b"storage_statistics_update"]) -> None: ...

global___Patch = Patch

@typing_extensions.final
class JobResult(google.protobuf.message.Message):
    """Result of a job.
    NEXT_ID: 2
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[JobResult._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATE_UNSPECIFIED: JobResult._State.ValueType  # 0
        SUCCEEDED: JobResult._State.ValueType  # 1
        FAILED: JobResult._State.ValueType  # 2
        SKIPPED: JobResult._State.ValueType  # 3

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    STATE_UNSPECIFIED: JobResult.State.ValueType  # 0
    SUCCEEDED: JobResult.State.ValueType  # 1
    FAILED: JobResult.State.ValueType  # 2
    SKIPPED: JobResult.State.ValueType  # 3

    STATE_FIELD_NUMBER: builtins.int
    STORAGE_STATISTICS_UPDATE_FIELD_NUMBER: builtins.int
    state: global___JobResult.State.ValueType
    @property
    def storage_statistics_update(self) -> space.core.proto.metadata_pb2.StorageStatistics:
        """The change of the storage statistics."""
    def __init__(
        self,
        *,
        state: global___JobResult.State.ValueType = ...,
        storage_statistics_update: space.core.proto.metadata_pb2.StorageStatistics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["storage_statistics_update", b"storage_statistics_update"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["state", b"state", "storage_statistics_update", b"storage_statistics_update"]) -> None: ...

global___JobResult = JobResult
