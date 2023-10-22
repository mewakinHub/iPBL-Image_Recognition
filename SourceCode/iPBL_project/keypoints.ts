/**
 * @license
 * Copyright 2020 Google LLC. All Rights Reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * =============================================================================
 */

// dictionary = key-value pair valueis list of key point
export const MESH_ANNOTATIONS: {[key: string]: number[]} = {
  silhouette: [
    10,  338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
    397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
    172, 58,  132, 93,  234, 127, 162, 21,  54,  103, 67,  109
  ],

  lipsUpperOuter: [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291],
  lipsLowerOuter: [146, 91, 181, 84, 17, 314, 405, 321, 375, 291],
  lipsUpperInner: [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308],
  lipsLowerInner: [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308],

  rightEyeUpper0: [246, 161, 160, 159, 158, 157, 173],
  rightEyeLower0: [33, 7, 163, 144, 145, 153, 154, 155, 133],
  rightEyeUpper1: [247, 30, 29, 27, 28, 56, 190],
  rightEyeLower1: [130, 25, 110, 24, 23, 22, 26, 112, 243],
  rightEyeUpper2: [113, 225, 224, 223, 222, 221, 189],
  rightEyeLower2: [226, 31, 228, 229, 230, 231, 232, 233, 244],
  rightEyeLower3: [143, 111, 117, 118, 119, 120, 121, 128, 245],

  rightEyebrowUpper: [156, 70, 63, 105, 66, 107, 55, 193],
  rightEyebrowLower: [35, 124, 46, 53, 52, 65],

  rightEyeIris: [473, 474, 475, 476, 477],

  leftEyeUpper0: [466, 388, 387, 386, 385, 384, 398],
  leftEyeLower0: [263, 249, 390, 373, 374, 380, 381, 382, 362],
  leftEyeUpper1: [467, 260, 259, 257, 258, 286, 414],
  leftEyeLower1: [359, 255, 339, 254, 253, 252, 256, 341, 463],
  leftEyeUpper2: [342, 445, 444, 443, 442, 441, 413],
  leftEyeLower2: [446, 261, 448, 449, 450, 451, 452, 453, 464],
  leftEyeLower3: [372, 340, 346, 347, 348, 349, 350, 357, 465],

  leftEyebrowUpper: [383, 300, 293, 334, 296, 336, 285, 417],
  leftEyebrowLower: [265, 353, 276, 283, 282, 295],

  leftEyeIris: [468, 469, 470, 471, 472],

  midwayBetweenEyes: [168],

  noseTip: [1],
  noseBottom: [2],
  noseRightCorner: [98],
  noseLeftCorner: [327],

  rightCheek: [205],
  leftCheek: [425],

  foreheadUpperOuter: [152,21,54,103,67,109,10,338,297,332,284,251,389],
  foreheadLowerOuter: [34,143,35,124,46,53,52,65,55,8,285,295,282,283,276,353,265,372,264],
  foreheadUpperInner: [139,71,68,104,69,108,151,337,299,333,298,301,368],
  foreheadLowerInner: [156,70,63,105,66,107,9,336,296,334,293,300,383],

  rightCheekUpperOuter: [93,234,127,34,143,111,117,118,101,36],
  rightCheekLowerOuter: [132,58,172,138,135,214,212,216,206],
  rightCheekUpperInner1: [227,116],
  rightCheekLowerInner1: [177,213,147,187,205],
  rightCheekUpperInner2: [137,123,50],
  rightCheekLowerInner2: [215,192,207],

  leftCheekUpperOuter: [266,330,347,346,340,372,264,356,454,323,],
  leftCheekLowerOuter: [426,436,432,434,364,367,397,288,361],
  leftCheekUpperInner1: [345,447],
  leftCheekLowerInnerr1: [425,411,376,433,401],
  leftCheekUpperInner2: [280,352,366],
  leftCheekLowerInner2: [427,416,435],

  upperLipUpperOuter: [61,185,40,39,37,0,267,269,270,409,291],
  upperLipLowerOuter: [78,191,80,81,82,13,312,311,310,415,308],
  upperLipUpperInner: [76,184,74,73,72,11,302,303,304,408,306],
  upperLipLowerInner: [62,183,42,41,38,12,268,271,272,407,292],

  lowerLipUpperOuter: [95,88,178,87,14,317,402,318,324,],
  lowerLipLowerOuter: [146,91,181,84,17,314,405,321,375],
  lowerLipUpperInner: [96,89,179,86,15,316,403,319,325],
  lowerLipLowerInner: [77,90,180,85,16,315,404,320,307],
  chinLowerOuter: [57,212,214,135,136,150,140,176,148,152,377,400,378,379,365,364,434,432,287],
  chinInner1: [43,106,182,83,18,313,406,335,273],
  chinInner2: [202,204,194,201,200,421,418,424,422],
  chinInner3: [210,211,32,208,199,428,262,431,430],
  chinInner4: [169,170,140,171,175,396,369,395,394]
};
