# Copyright 2018 Tensorforce Team. All Rights Reserved.
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

import tensorflow as tf

from tensorforce import TensorforceError, util
from tensorforce.core.parameters import Parameter


class Constant(Parameter):
    """
    Constant hyperparameter.
    """

    # Argument 'value' first for default specification
    def __init__(self, name, value, dtype=None, summary_labels=None):
        if dtype is None:
            if isinstance(value, bool):
                dtype = 'bool'
            elif isinstance(value, int):
                dtype = 'int'
            elif isinstance(value, float):
                dtype = 'float'
            else:
                raise TensorforceError.unexpected()

        super().__init__(name=name, dtype=dtype, shape=(), summary_labels=summary_labels)

        self.constant_value = value

    def get_parameter_value(self):
        parameter = tf.constant(value=self.constant_value, dtype=util.tf_dtype(dtype=self.dtype))

        return parameter
