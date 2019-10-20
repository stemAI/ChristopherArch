#
#                                                  -.   .ohysssds-   -.                                                  
#                                                   \\ `NMMoNmhmMM. //                                                   
#                                                    \\ mNssNmm/dN.//                                         
#     :ohddhsyys//:.-.                                  ohhsydd+:/:                               .-.:/soyhyhmhhy+.    
#   +yhhysdd:+:+/-+///++:/::/-.`                       .ss:+ossysy                         .-::/+++/++//+++//oshmmMNs   
#   +hdydhs+-/+-+++///+/+:+oydNNMhhso/:---.-..`    `+../++`:s++yhd-..o.      ...----:/++sssdyy/:o/++/+-+oo.////yyhddmh   
#    .syNs:++++++/+////++++oohmhdmMNh:+/o+++++.o/-::--.//+`:s/+ydm-..-.:-:/+o/:o/+o++symNNdmyso/+-+:/+:/+//o:+:+syhd+`   
#       /++/++/+/+++/+++oo+++ssdmmNmyo+//+-++sNdhhhyyoo//so+syhddyoosssodddyoo++++/+yysddmMdys++o++++o+///+//++sss-      
#         .://:///+/o+/+/-+++++symN+oo++/o++/+yhyddhysyhyhddNMmyhhyyyhmsyhyhso/++++//oydNMNd/++///++//+o/:://::.         
#             -:++/++///-:/-:/o/+so+/+-+/+////+/+//+s+++dhs+o+ohhyo++++o/+++o+s+o++++oodmmho///+-/+:+-/-o/:-`            
#                  ..::://////-//-::.-/-/.::-/-+++///:.-hyshNmshdy-.://///:::::/:/:://+///////:-/:---..`                 
#                                     `..:/:+/ooo/s+hmddddmyhdmydhho+o:/+:/o:/:-.-.`                                     
#          ..-.--.----:::::/++++/:///o+/+/:::yymNmmNdyss/-oddNNs/hdmdmdmmmdyyo+++++/++//:::.::-::.-.-.--.--.::--`        
#     .+hhso/+//+//+/++/++/syNmyo:++:/+/++o/ohhdmyyooo+o:oo+ooyosoo++++ommMhms/+////o+ymhdmNdso+/+o/:////-/:/+syhhs/`    
#   :yhNss++///++o/o++:/o++yNMMhoo/+++///+:/++s+o+//++/./ys++/oyd+:+/++/+-s++++/++//:++ydmddso+++-oooosso/o+/+++yhhyhs-  
#   Nmhdmh+ooo+++/o/+/+:+++:dMNo/+:////+-//:++/+:////:: /hy:`:+sho :o/+++/o//++/+//++:+/dmmh-o+o++:++++oo++ssooosydhhh+  
#    .:/soo++++/++////+///++sdd++-+:///+:++-//+/::+//:  /yh/-/+ydo  .oo+++++/-+/o/::/+:+yho+/+////o//++++++o+s+/+yyo/`   
#                //oo:+//+//-/:///.:-///:+:+/o+./::-`   /hs://osy+    :+oo++/s+:///+/-+//o//++-s++/++://+/-:          
#                                                       :yy---osh/                  
#                                                       /oy///sdo:                                                       
#                                                       .yy: -+ys-                                                       
#                                                        ys+:/ohs`                                                       
#                                                        +y/`.+yy                                                        
#                                                        :os//sy:                                                        
#                                                        .ss::ys-                                                        
#                                                         +s::sy-                                                        
#                                                         +o/:hy`                                                        
#                                                         :o/oh:                                                         
#                                                         `y-os-                                                         
#                                                          /y+o-                                                         
#                                                          .s/s                                                          
#                                                           oo:                                                          
#                                                                                                                        
#                                        
                                                                                                                        
                                                                                                                        
                                                                                                          
# Edits for personlised use by Oleic 
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

# Bring in all of the public TensorFlow interface into this
# module.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=g-bad-import-order
from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import

from tensorflow.python.util.lazy_loader import LazyLoader
contrib = LazyLoader('contrib', globals(), 'tensorflow.contrib')
del LazyLoader

from tensorflow.python.platform import flags  # pylint: disable=g-import-not-at-top
from tensorflow.python.platform import app  # pylint: disable=g-import-not-at-top
app.flags = flags

del absolute_import
del division
del print_function

# These symbols appear because we import the python package which
# in turn imports from tensorflow.core and tensorflow.python. They
# must come from this module. So python adds these symbols for the
# resolution to succeed.
# pylint: disable=undefined-variable
del python
del core
# pylint: enable=undefined-variable
