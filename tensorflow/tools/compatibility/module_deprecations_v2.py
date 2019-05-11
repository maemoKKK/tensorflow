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
"""Module deprecation warnings for TensorFlow 2.0."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.tools.compatibility import ast_edits


_CONTRIB_WARNING = (
    ast_edits.ERROR,
    "<function name> cannot be converted automatically. tf.contrib will not"
    " be distributed with TensorFlow 2.0, please consider an alternative in"
    " non-contrib TensorFlow, a community-maintained repository, or fork "
    "the required code."
)

_FLAGS_WARNING = (
    ast_edits.ERROR,
    "tf.flags has been removed, please use the argparse or absl"
    " modules if you need command line parsing."
)

_CONTRIB_CUDNN_RNN_WARNING = (
    ast_edits.WARNING,
    "(Manual edit required) tf.contrib.cudnn_rnn.* has been deprecated, "
    "and the CuDNN kernel has been integrated with "
    "tf.keras.layers.LSTM/GRU in TensorFlow 2.0. Please check the new API "
    "and use that instead."
)

_CONTRIB_RNN_WARNING = (
    ast_edits.WARNING,
    "(Manual edit required) tf.contrib.rnn.* has been deprecated, and "
    "widely used cells/functions will be moved to tensorflow/addons "
    "repository. Please check it there and file Github issues if necessary."
)

_CONTRIB_DIST_STRAT_WARNING = (
    ast_edits.WARNING,
    "(Manual edit required) tf.contrib.distribute.* have been migrated to"
    "tf.distribute.*. Please check out the new module for updates APIs.")

MODULE_DEPRECATIONS = {
    "tf.contrib": _CONTRIB_WARNING,
    "tf.contrib.cudnn_rnn": _CONTRIB_CUDNN_RNN_WARNING,
    "tf.contrib.rnn": _CONTRIB_RNN_WARNING,
    "tf.flags": _FLAGS_WARNING,
    "tf.contrib.distribute": _CONTRIB_DIST_STRAT_WARNING
}