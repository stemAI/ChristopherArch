# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""TraceMe allows the profiler to trace python events.

Usage:
    with profiler.TraceMe('name'):
      ...
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python import pywrap_tensorflow
from tensorflow.python.util.tf_export import tf_export


@tf_export('profiler.TraceMe')
class TraceMe(object):
  """Context manager that generates a trace event in the profiler."""

  def __init__(self, name):
    self._traceme = pywrap_tensorflow.PythonTraceMe(name)

  def __enter__(self):
    self._traceme.Enter()

  def __exit__(self, exc_type, exc_val, exc_tb):
    self._traceme.Exit()
