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

"""
TODO
"""

import inspect

import pyspark.context
import pyspark.rdd

from .context import EsSparkContext, monkey_patch_sc
from .rdd import saveToEs, saveJsonToEs


__all__ = [
    "EsSparkContext",
]

# Monkey patch the default python RDD so that it can be stored to Elastic Search as documents
pyspark.rdd.RDD.saveToEs = saveToEs
pyspark.rdd.RDD.saveJsonToEs = saveJsonToEs

# Monkey patch the sc variable in the caller if any
parent_frame = inspect.currentframe().f_back
if "sc" in parent_frame.f_globals:
	monkey_patch_sc(parent_frame.f_globals["sc"])
