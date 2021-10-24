# -*- coding: utf-8 -*-
#
#         PySceneDetect: Python-Based Video Scene Detector
#   ---------------------------------------------------------------
#     [  Site: http://www.bcastell.com/projects/PySceneDetect/   ]
#     [  Github: https://github.com/Breakthrough/PySceneDetect/  ]
#     [  Documentation: http://pyscenedetect.readthedocs.org/    ]
#
# Copyright (C) 2014-2021 Brandon Castellano <http://www.bcastell.com>.
#
# PySceneDetect is licensed under the BSD 3-Clause License; see the included
# LICENSE file, or visit one of the following pages for details:
#  - https://github.com/Breakthrough/PySceneDetect/
#  - http://www.bcastell.com/projects/PySceneDetect/
#
# This software uses Numpy, OpenCV, click, tqdm, simpletable, and pytest.
# See the included LICENSE files or one of the above URLs for more information.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

""" PySceneDetect API Test

Usage: Run as part of standard test suite, but can be manually invoked
by passing the video file to perform scene detection on as an argument
to this file, e.g. `python test_api.py SOME_VIDEO.mp4`

"""

from __future__ import print_function
import os
import sys

import scenedetect
from scenedetect.backends.opencv import VideoStreamCv2
from scenedetect import SceneManager
from scenedetect import StatsManager
from scenedetect.detectors import ContentDetector

STATS_FILE_PATH = 'api_test_statsfile.csv'

#
# TODO: Add more comprehensive test cases to act as examples.
#

def test_api(test_video_file):
    # (str) -> None
    """ Test overall PySceneDetect API functionality.

    Can be considered a high level integration/black-box test.

    """

    print("Running PySceneDetect API test...")

    print("PySceneDetect version being used: %s" % str(scenedetect.__version__))

    video = VideoStreamCv2(test_video_file)
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)
    # Add ContentDetector algorithm (constructor takes detector options like threshold).
    scene_manager.add_detector(ContentDetector())
    base_timecode = video.base_timecode

    # If stats file exists, load it.
    if os.path.exists(STATS_FILE_PATH):
        # Read stats from CSV file opened in read mode:
        with open(STATS_FILE_PATH, 'r') as stats_file:
            stats_manager.load_from_csv(stats_file)

    start_time = base_timecode + 20     # 00:00:00.667
    end_time = base_timecode + 20.0     # 00:00:20.000

    # Set downscale factor to improve processing speed.
    scene_manager.auto_downscale = True

    # Perform scene detection on video.
    video.seek(start_time)
    scene_manager.detect_scenes(video=video, end_time=end_time)

    # Obtain list of detected scenes.
    scene_list = scene_manager.get_scene_list()
    # Like FrameTimecodes, each scene in the scene_list can be sorted if the
    # list of scenes becomes unsorted.

    print('List of scenes obtained:')
    for i, scene in enumerate(scene_list):
        print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
            i+1,
            scene[0].get_timecode(), scene[0].get_frames(),
            scene[1].get_timecode(), scene[1].get_frames(),))

    # We only write to the stats file if a save is required:
    if stats_manager.is_save_required():
        with open(STATS_FILE_PATH, 'w') as stats_file:
            stats_manager.save_to_csv(stats_file, base_timecode)



# Support running as a stand-alone file.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: %s [TEST_VIDEO_FILE]' % sys.argv[0])
    else:
        test_api(sys.argv[1])