def findRelativeRanks(score):
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    score_map = dict()
    for i, j in enumerate(sorted(score, reverse=True)):
        if i <= 2:
            score_map[j] = medals[i]
        else:
            score_map[j] = i + 1

    ans = []
    for i in score:
        ans.append(score_map[i])
    
    return ans


score = [5,4,3,2,1]
print(findRelativeRanks(score))

score = [10,3,8,9,4]
print(findRelativeRanks(score))

score = [4536,4658,2036,4322,1869,52,5085,1504,2493,3231,1041,3699,2443,4406,4989,2089,1782,5428,960,4882,1481,1673,1244,2801,1814,1893,3552,1277,2308,3425,4407,1647,561,3228,1029,5320,3292,3138,1294,262,5053,4462,3367,5192,5447,656,4105,178,1775,5158,5032,418,2963,2936,3263,2882,5260,762,2325,5048,5366,3211,2227,1961,4343,121,4475,991,4272,3713,1435,927,5054,2761,2877,3055,5515,1328,3671,477,5116,2816,1219,1747,4941,1069,725,3991,2394,797,1646,3243,3201,4795,4334,3537,4136,2854,2155,558,1113,4277,2680,3532,3934,4731,3728,534,2131,3860,2263,3203,639,2236,5430,648,1264,3977,783,5024,5030,1836,436,3630,2033,2243,5437,2790,3380,3402,2163,1689,3286,92,1662,4838,3241,4807,16,3119,3701,1534,5218,3375,1778,997,1249,1972,5166,1159,774,3968,5026,4229,3325,1728,1589,1759,491,1632,3229,1528,2233,3830,636,163,1645,4839,224,3418,2115,712,246,5037,1881,5075,284,3472,366,1963,2529,643,3513,319,999,2590,4187,3885,1494,4992,3401,1804,1863,5057,3775,2178,635,5100,3503,1020,2466,5488,700,5491,3894,3320,806,3194,4791,4607,3010,5400,1068,4771,622,3143,4501,2907,887,4939,3342,1102,4527,1336,2933,3727,5324,4325,2728,4751,465,2062,430,78,5292,1592,3189,969,82,4873,4076,5322,1403,2194,5388,1677,357,3628,2031,5225,3634,2037,1320,3789,2195,1949,1138,4279,5076,1431,4625,1038,3648,2051,2436,4033,839,3230,109,4454,466,2063,1184,614,2840,1243,4600,5336,2142,1741,144,5073,3476,1005,4990,2853,1259,1901,4298,1104,3193,2396,3118,1524,2547,950,4918,3321,4835,44,1641,326,4537,1344,4538,1829,3957,1255,5504,685,3979,2480,3223,1626,4455,1791,4492,3255,1966,901,4089,4006,836,2427,4024,4646,1048,1042,4236,504,4855,3258,64,4049,3249,4846,448,3636,2597,1000,5445,3389,4986,2703,4084,2487,2222,1973,3570,1422,4616,20,867,4055,3810,5407,445,5236,1092,1892,295,4127,653,559,828,796,3984,87,2478,3603,2913,3291,2429,952,5391,2197,5387,4244,2647,4048,3144,1547,717,3403,1806,4197,3215,1618,862,1880,283,3889,695,1397,2787,4709,3912,3654,2060,2504,4101,5452,3064,4661,1467,2814,4411,2817,2020,2653,1056,3447,73,4864,2998,1642,157,2548,954,2674,4271,1077,1874,4494,1300,497,3691,1444,3838,2241,3832,5429,3798,604,1060,5338,556,4532,2938,660,2692,1095,4283,3880,5474,2108,511,2367,770,714,1511,1487,690,5247,456,2847,3100,4028,3221,3770,5367,1376,4570,4100,4897,1937,2734,5175,3578,5172,3540,2265,3862,2418,3437,243,3410,5007,4427,1648,5138,350,3544,1122,4316,5003,5436,1451,3354,4157,963,4708,2317,112,4894,909,4834,4907,2528,1731,4703,5142,4308,2714,314,5105,3511,323,1550,808,1560,3289,4086,213,2604,4880,4618,3821,2230,633,3412,2649,2926,1332,5140,2333,736,4724,3127,2327,3924,5036,2476,782,3976,3179,3176,4770,2376,3973,2862,1447,4539,1630,3224,2836,5156,3562,4644,4642,1448,3216,1625,28,1622,4013,5520,738,4723,3929,2332,4310,3136,1539,742,5121,3530,1933,1133,2727,1578,3969,4313,2356,759,4747,3150,1833,2782,1985,4663,1987,4653,3059,1074,2010,3474,487,2084,4466,2915,5312,3715,2121,3743,4540,2946,2555,961,2453,859,2072,591,5373,588,2185,682,2276,1639,1714,1711,3308,1708,4902,5308,1323,1811,3796,4650,3053,2068,5262,2071,3668,1228,5213,2522,4116,1463,4657,3063,18,3206,4003,1218,2812,5489,3470,247,4931,3334,290,4275,2681,3901,3104,1510,904,3295,1707,680,5471,5083,1379,579,2176,2182,4973,1779,1362,5356,565,2754,4739,3453,5047,265,2742,4336,1148,3387,193,1790,587,4581,4584,2987,1393,2584,1262,858,3649,461,2437,4034,2218,3815,3358,4952,3748,2151,4622,5419,1446,3037,4167,976,1767,4961,5051,745,5130,1067,4255,270,2526,2923,2723,4714,3120,1139,5124,3749,4934,4909,4284,2687,3093,1496,46,5187,3599,2408,3282,4879,2491,894,4664,3085,694,273,3846,3809,1418,5080,1886,3089,4686,1498,5264,482,1279,5031,2637,4234,3165,1568,3950,2210,100,4054,2369,772,3948,1554,4742,4388,2794,412,974,2168,1371,1812,4203,2610,5001,2864,392,389,1986,1189,3580,3777,450,4417,3620,2035,1238,4993,1417,4605,2214,3423,229,1572,4760,3694,5079,3485,3494,1897,2568,971,3359,1765,965,4950,2559,4025,4349,1958,370,3943,2564,2767,1364,2958,4186,3786,801,3192,5201,410,1207,395,3589,4519,1331,3217,1096,1699,3296,4093,4866,4041,2465,74,3647,3079,2109,124,612,1006,2323,726,2908,920,2517,923,3057,4568,2974,3771,3374,2271,3868,1143,4689,105,2890,5290,2899,3302,4099,1908,4305,1111,708,3893,1502,371,3565,3568,5165,1971,1186,4774,3180,2383,789,486,3438,2863,4460,1690,93,5327,2139,353,747,4166,4775,3181,4179,1785,4726,3576,4373,4470,391,3585,5191,383,4371,2957,3754,1357,4551,2160,1847,2838,4044,59,4285,1097,4685,1442,2167,573,5326,219,1816,5010,1834,1831,5019,1034,222,2762,398]
print(findRelativeRanks(score))