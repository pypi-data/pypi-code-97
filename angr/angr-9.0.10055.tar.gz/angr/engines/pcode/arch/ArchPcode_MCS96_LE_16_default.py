###
### This file was automatically generated
###

from archinfo.arch import register_arch, Endness, Register

from .common import ArchPcode


class ArchPcode_MCS96_LE_16_default(ArchPcode):
    name = 'MCS96:LE:16:default'
    pcode_arch = 'MCS96:LE:16:default'
    description = 'Intel MCS-96 Microcontroller Family'
    bits = 16
    ip_offset = 0x10
    sp_offset = 0x18
    bp_offset = sp_offset
    instruction_endness = Endness.LE
    register_list = [
        Register('zr_ad', 4, 0x0),
        Register('zr', 2, 0x0),
        Register('zrlo', 1, 0x0),
        Register('zrhi', 1, 0x1),
        Register('ad_result', 2, 0x2),
        Register('ad_resultlo', 1, 0x2),
        Register('ad_resulthi', 1, 0x3),
        Register('hsi', 4, 0x4),
        Register('hsi_time', 2, 0x4),
        Register('hsi_timelo', 1, 0x4),
        Register('hsi_timehi', 1, 0x5),
        Register('hsi_sbuf', 2, 0x6),
        Register('hsi_status', 1, 0x6),
        Register('sbuf', 1, 0x7),
        Register('int_timer1', 4, 0x8),
        Register('interrupt', 2, 0x8),
        Register('int_mask', 1, 0x8),
        Register('int_pend', 1, 0x9),
        Register('timer1', 2, 0xa),
        Register('timer1lo', 1, 0xa),
        Register('timer1hi', 1, 0xb),
        Register('timer2_port01', 4, 0xc),
        Register('timer2', 2, 0xc),
        Register('timer2lo', 1, 0xc),
        Register('timer2hi', 1, 0xd),
        Register('port01', 2, 0xe),
        Register('port0', 1, 0xe),
        Register('port1', 1, 0xf),
        Register('port2_int1', 4, 0x10),
        Register('port2_sps', 2, 0x10),
        Register('port2', 1, 0x10),
        Register('sp_stat', 1, 0x11),
        Register('int1', 2, 0x12),
        Register('int_pend1', 1, 0x12),
        Register('int_mask1', 1, 0x13),
        Register('wsr_ios012', 4, 0x14),
        Register('wsr_ios0', 2, 0x14),
        Register('wsr', 1, 0x14),
        Register('ios0', 1, 0x15),
        Register('ios12', 2, 0x16),
        Register('ios1', 1, 0x16),
        Register('ios2', 1, 0x17),
        Register('spr1a', 4, 0x18),
        Register('spr', 2, 0x18),
        Register('splo', 1, 0x18),
        Register('sphi', 1, 0x19),
        Register('rw1a', 2, 0x1a),
        Register('r1a', 1, 0x1a),
        Register('r1b', 1, 0x1b),
        Register('rl1c', 4, 0x1c),
        Register('rw1c', 2, 0x1c),
        Register('r1c', 1, 0x1c),
        Register('r1d', 1, 0x1d),
        Register('rw1e', 2, 0x1e),
        Register('r1e', 1, 0x1e),
        Register('r1f', 1, 0x1f),
        Register('rl20', 4, 0x20),
        Register('rw20', 2, 0x20),
        Register('r20', 1, 0x20),
        Register('r21', 1, 0x21),
        Register('rw22', 2, 0x22),
        Register('r22', 1, 0x22),
        Register('r23', 1, 0x23),
        Register('rl24', 4, 0x24),
        Register('rw24', 2, 0x24),
        Register('r24', 1, 0x24),
        Register('r25', 1, 0x25),
        Register('rw26', 2, 0x26),
        Register('r26', 1, 0x26),
        Register('r27', 1, 0x27),
        Register('rl28', 4, 0x28),
        Register('rw28', 2, 0x28),
        Register('r28', 1, 0x28),
        Register('r29', 1, 0x29),
        Register('rw2a', 2, 0x2a),
        Register('r2a', 1, 0x2a),
        Register('r2b', 1, 0x2b),
        Register('rl2c', 4, 0x2c),
        Register('rw2c', 2, 0x2c),
        Register('r2c', 1, 0x2c),
        Register('r2d', 1, 0x2d),
        Register('rw2e', 2, 0x2e),
        Register('r2e', 1, 0x2e),
        Register('r2f', 1, 0x2f),
        Register('rl30', 4, 0x30),
        Register('rw30', 2, 0x30),
        Register('r30', 1, 0x30),
        Register('r31', 1, 0x31),
        Register('rw32', 2, 0x32),
        Register('r32', 1, 0x32),
        Register('r33', 1, 0x33),
        Register('rl34', 4, 0x34),
        Register('rw34', 2, 0x34),
        Register('r34', 1, 0x34),
        Register('r35', 1, 0x35),
        Register('rw36', 2, 0x36),
        Register('r36', 1, 0x36),
        Register('r37', 1, 0x37),
        Register('rl38', 4, 0x38),
        Register('rw38', 2, 0x38),
        Register('r38', 1, 0x38),
        Register('r39', 1, 0x39),
        Register('rw3a', 2, 0x3a),
        Register('r3a', 1, 0x3a),
        Register('r3b', 1, 0x3b),
        Register('rl3c', 4, 0x3c),
        Register('rw3c', 2, 0x3c),
        Register('r3c', 1, 0x3c),
        Register('r3d', 1, 0x3d),
        Register('rw3e', 2, 0x3e),
        Register('r3e', 1, 0x3e),
        Register('r3f', 1, 0x3f),
        Register('rl40', 4, 0x40),
        Register('rw40', 2, 0x40),
        Register('r40', 1, 0x40),
        Register('r41', 1, 0x41),
        Register('rw42', 2, 0x42),
        Register('r42', 1, 0x42),
        Register('r43', 1, 0x43),
        Register('rl44', 4, 0x44),
        Register('rw44', 2, 0x44),
        Register('r44', 1, 0x44),
        Register('r45', 1, 0x45),
        Register('rw46', 2, 0x46),
        Register('r46', 1, 0x46),
        Register('r47', 1, 0x47),
        Register('rl48', 4, 0x48),
        Register('rw48', 2, 0x48),
        Register('r48', 1, 0x48),
        Register('r49', 1, 0x49),
        Register('rw4a', 2, 0x4a),
        Register('r4a', 1, 0x4a),
        Register('r4b', 1, 0x4b),
        Register('rl4c', 4, 0x4c),
        Register('rw4c', 2, 0x4c),
        Register('r4c', 1, 0x4c),
        Register('r4d', 1, 0x4d),
        Register('rw4e', 2, 0x4e),
        Register('r4e', 1, 0x4e),
        Register('r4f', 1, 0x4f),
        Register('rl50', 4, 0x50),
        Register('rw50', 2, 0x50),
        Register('r50', 1, 0x50),
        Register('r51', 1, 0x51),
        Register('rw52', 2, 0x52),
        Register('r52', 1, 0x52),
        Register('r53', 1, 0x53),
        Register('rl54', 4, 0x54),
        Register('rw54', 2, 0x54),
        Register('r54', 1, 0x54),
        Register('r55', 1, 0x55),
        Register('rw56', 2, 0x56),
        Register('r56', 1, 0x56),
        Register('r57', 1, 0x57),
        Register('rl58', 4, 0x58),
        Register('rw58', 2, 0x58),
        Register('r58', 1, 0x58),
        Register('r59', 1, 0x59),
        Register('rw5a', 2, 0x5a),
        Register('r5a', 1, 0x5a),
        Register('r5b', 1, 0x5b),
        Register('rl5c', 4, 0x5c),
        Register('rw5c', 2, 0x5c),
        Register('r5c', 1, 0x5c),
        Register('r5d', 1, 0x5d),
        Register('rw5e', 2, 0x5e),
        Register('r5e', 1, 0x5e),
        Register('r5f', 1, 0x5f),
        Register('rl60', 4, 0x60),
        Register('rw60', 2, 0x60),
        Register('r60', 1, 0x60),
        Register('r61', 1, 0x61),
        Register('rw62', 2, 0x62),
        Register('r62', 1, 0x62),
        Register('r63', 1, 0x63),
        Register('rl64', 4, 0x64),
        Register('rw64', 2, 0x64),
        Register('r64', 1, 0x64),
        Register('r65', 1, 0x65),
        Register('rw66', 2, 0x66),
        Register('r66', 1, 0x66),
        Register('r67', 1, 0x67),
        Register('rl68', 4, 0x68),
        Register('rw68', 2, 0x68),
        Register('r68', 1, 0x68),
        Register('r69', 1, 0x69),
        Register('rw6a', 2, 0x6a),
        Register('r6a', 1, 0x6a),
        Register('r6b', 1, 0x6b),
        Register('rl6c', 4, 0x6c),
        Register('rw6c', 2, 0x6c),
        Register('r6c', 1, 0x6c),
        Register('r6d', 1, 0x6d),
        Register('rw6e', 2, 0x6e),
        Register('r6e', 1, 0x6e),
        Register('r6f', 1, 0x6f),
        Register('rl70', 4, 0x70),
        Register('rw70', 2, 0x70),
        Register('r70', 1, 0x70),
        Register('r71', 1, 0x71),
        Register('rw72', 2, 0x72),
        Register('r72', 1, 0x72),
        Register('r73', 1, 0x73),
        Register('rl74', 4, 0x74),
        Register('rw74', 2, 0x74),
        Register('r74', 1, 0x74),
        Register('r75', 1, 0x75),
        Register('rw76', 2, 0x76),
        Register('r76', 1, 0x76),
        Register('r77', 1, 0x77),
        Register('rl78', 4, 0x78),
        Register('rw78', 2, 0x78),
        Register('r78', 1, 0x78),
        Register('r79', 1, 0x79),
        Register('rw7a', 2, 0x7a),
        Register('r7a', 1, 0x7a),
        Register('r7b', 1, 0x7b),
        Register('rl7c', 4, 0x7c),
        Register('rw7c', 2, 0x7c),
        Register('r7c', 1, 0x7c),
        Register('r7d', 1, 0x7d),
        Register('rw7e', 2, 0x7e),
        Register('r7e', 1, 0x7e),
        Register('r7f', 1, 0x7f),
        Register('rl80', 4, 0x80),
        Register('rw80', 2, 0x80),
        Register('r80', 1, 0x80),
        Register('r81', 1, 0x81),
        Register('rw82', 2, 0x82),
        Register('r82', 1, 0x82),
        Register('r83', 1, 0x83),
        Register('rl84', 4, 0x84),
        Register('rw84', 2, 0x84),
        Register('r84', 1, 0x84),
        Register('r85', 1, 0x85),
        Register('rw86', 2, 0x86),
        Register('r86', 1, 0x86),
        Register('r87', 1, 0x87),
        Register('rl88', 4, 0x88),
        Register('rw88', 2, 0x88),
        Register('r88', 1, 0x88),
        Register('r89', 1, 0x89),
        Register('rw8a', 2, 0x8a),
        Register('r8a', 1, 0x8a),
        Register('r8b', 1, 0x8b),
        Register('rl8c', 4, 0x8c),
        Register('rw8c', 2, 0x8c),
        Register('r8c', 1, 0x8c),
        Register('r8d', 1, 0x8d),
        Register('rw8e', 2, 0x8e),
        Register('r8e', 1, 0x8e),
        Register('r8f', 1, 0x8f),
        Register('rl90', 4, 0x90),
        Register('rw90', 2, 0x90),
        Register('r90', 1, 0x90),
        Register('r91', 1, 0x91),
        Register('rw92', 2, 0x92),
        Register('r92', 1, 0x92),
        Register('r93', 1, 0x93),
        Register('rl94', 4, 0x94),
        Register('rw94', 2, 0x94),
        Register('r94', 1, 0x94),
        Register('r95', 1, 0x95),
        Register('rw96', 2, 0x96),
        Register('r96', 1, 0x96),
        Register('r97', 1, 0x97),
        Register('rl98', 4, 0x98),
        Register('rw98', 2, 0x98),
        Register('r98', 1, 0x98),
        Register('r99', 1, 0x99),
        Register('rw9a', 2, 0x9a),
        Register('r9a', 1, 0x9a),
        Register('r9b', 1, 0x9b),
        Register('rl9c', 4, 0x9c),
        Register('rw9c', 2, 0x9c),
        Register('r9c', 1, 0x9c),
        Register('r9d', 1, 0x9d),
        Register('rw9e', 2, 0x9e),
        Register('r9e', 1, 0x9e),
        Register('r9f', 1, 0x9f),
        Register('rla0', 4, 0xa0),
        Register('rwa0', 2, 0xa0),
        Register('ra0', 1, 0xa0),
        Register('ra1', 1, 0xa1),
        Register('rwa2', 2, 0xa2),
        Register('ra2', 1, 0xa2),
        Register('ra3', 1, 0xa3),
        Register('rla4', 4, 0xa4),
        Register('rwa4', 2, 0xa4),
        Register('ra4', 1, 0xa4),
        Register('ra5', 1, 0xa5),
        Register('rwa6', 2, 0xa6),
        Register('ra6', 1, 0xa6),
        Register('ra7', 1, 0xa7),
        Register('rla8', 4, 0xa8),
        Register('rwa8', 2, 0xa8),
        Register('ra8', 1, 0xa8),
        Register('ra9', 1, 0xa9),
        Register('rwaa', 2, 0xaa),
        Register('raa', 1, 0xaa),
        Register('rab', 1, 0xab),
        Register('rlac', 4, 0xac),
        Register('rwac', 2, 0xac),
        Register('rac', 1, 0xac),
        Register('rad', 1, 0xad),
        Register('rwae', 2, 0xae),
        Register('rae', 1, 0xae),
        Register('raf', 1, 0xaf),
        Register('rlb0', 4, 0xb0),
        Register('rwb0', 2, 0xb0),
        Register('rb0', 1, 0xb0),
        Register('rb1', 1, 0xb1),
        Register('rwb2', 2, 0xb2),
        Register('rb2', 1, 0xb2),
        Register('rb3', 1, 0xb3),
        Register('rlb4', 4, 0xb4),
        Register('rwb4', 2, 0xb4),
        Register('rb4', 1, 0xb4),
        Register('rb5', 1, 0xb5),
        Register('rwb6', 2, 0xb6),
        Register('rb6', 1, 0xb6),
        Register('rb7', 1, 0xb7),
        Register('rlb8', 4, 0xb8),
        Register('rwb8', 2, 0xb8),
        Register('rb8', 1, 0xb8),
        Register('rb9', 1, 0xb9),
        Register('rwba', 2, 0xba),
        Register('rba', 1, 0xba),
        Register('rbb', 1, 0xbb),
        Register('rlbc', 4, 0xbc),
        Register('rwbc', 2, 0xbc),
        Register('rbc', 1, 0xbc),
        Register('rbd', 1, 0xbd),
        Register('rwbe', 2, 0xbe),
        Register('rbe', 1, 0xbe),
        Register('rbf', 1, 0xbf),
        Register('rlc0', 4, 0xc0),
        Register('rwc0', 2, 0xc0),
        Register('rc0', 1, 0xc0),
        Register('rc1', 1, 0xc1),
        Register('rwc2', 2, 0xc2),
        Register('rc2', 1, 0xc2),
        Register('rc3', 1, 0xc3),
        Register('rlc4', 4, 0xc4),
        Register('rwc4', 2, 0xc4),
        Register('rc4', 1, 0xc4),
        Register('rc5', 1, 0xc5),
        Register('rwc6', 2, 0xc6),
        Register('rc6', 1, 0xc6),
        Register('rc7', 1, 0xc7),
        Register('rlc8', 4, 0xc8),
        Register('rwc8', 2, 0xc8),
        Register('rc8', 1, 0xc8),
        Register('rc9', 1, 0xc9),
        Register('rwca', 2, 0xca),
        Register('rca', 1, 0xca),
        Register('rcb', 1, 0xcb),
        Register('rlcc', 4, 0xcc),
        Register('rwcc', 2, 0xcc),
        Register('rcc', 1, 0xcc),
        Register('rcd', 1, 0xcd),
        Register('rwce', 2, 0xce),
        Register('rce', 1, 0xce),
        Register('rcf', 1, 0xcf),
        Register('rld0', 4, 0xd0),
        Register('rwd0', 2, 0xd0),
        Register('rd0', 1, 0xd0),
        Register('rd1', 1, 0xd1),
        Register('rwd2', 2, 0xd2),
        Register('rd2', 1, 0xd2),
        Register('rd3', 1, 0xd3),
        Register('rld4', 4, 0xd4),
        Register('rwd4', 2, 0xd4),
        Register('rd4', 1, 0xd4),
        Register('rd5', 1, 0xd5),
        Register('rwd6', 2, 0xd6),
        Register('rd6', 1, 0xd6),
        Register('rd7', 1, 0xd7),
        Register('rld8', 4, 0xd8),
        Register('rwd8', 2, 0xd8),
        Register('rd8', 1, 0xd8),
        Register('rd9', 1, 0xd9),
        Register('rwda', 2, 0xda),
        Register('rda', 1, 0xda),
        Register('rdb', 1, 0xdb),
        Register('rldc', 4, 0xdc),
        Register('rwdc', 2, 0xdc),
        Register('rdc', 1, 0xdc),
        Register('rdd', 1, 0xdd),
        Register('rwde', 2, 0xde),
        Register('rde', 1, 0xde),
        Register('rdf', 1, 0xdf),
        Register('rle0', 4, 0xe0),
        Register('rwe0', 2, 0xe0),
        Register('re0', 1, 0xe0),
        Register('re1', 1, 0xe1),
        Register('rwe2', 2, 0xe2),
        Register('re2', 1, 0xe2),
        Register('re3', 1, 0xe3),
        Register('rle4', 4, 0xe4),
        Register('rwe4', 2, 0xe4),
        Register('re4', 1, 0xe4),
        Register('re5', 1, 0xe5),
        Register('rwe6', 2, 0xe6),
        Register('re6', 1, 0xe6),
        Register('re7', 1, 0xe7),
        Register('rle8', 4, 0xe8),
        Register('rwe8', 2, 0xe8),
        Register('re8', 1, 0xe8),
        Register('re9', 1, 0xe9),
        Register('rwea', 2, 0xea),
        Register('rea', 1, 0xea),
        Register('reb', 1, 0xeb),
        Register('rlec', 4, 0xec),
        Register('rwec', 2, 0xec),
        Register('rec', 1, 0xec),
        Register('red', 1, 0xed),
        Register('rwee', 2, 0xee),
        Register('ree', 1, 0xee),
        Register('ref', 1, 0xef),
        Register('rlf0', 4, 0xf0),
        Register('rwf0', 2, 0xf0),
        Register('rf0', 1, 0xf0),
        Register('rf1', 1, 0xf1),
        Register('rwf2', 2, 0xf2),
        Register('rf2', 1, 0xf2),
        Register('rf3', 1, 0xf3),
        Register('rlf4', 4, 0xf4),
        Register('rwf4', 2, 0xf4),
        Register('rf4', 1, 0xf4),
        Register('rf5', 1, 0xf5),
        Register('rwf6', 2, 0xf6),
        Register('rf6', 1, 0xf6),
        Register('rf7', 1, 0xf7),
        Register('rlf8', 4, 0xf8),
        Register('rwf8', 2, 0xf8),
        Register('rf8', 1, 0xf8),
        Register('rf9', 1, 0xf9),
        Register('rwfa', 2, 0xfa),
        Register('rfa', 1, 0xfa),
        Register('rfb', 1, 0xfb),
        Register('rlfc', 4, 0xfc),
        Register('rwfc', 2, 0xfc),
        Register('rfc', 1, 0xfc),
        Register('rfd', 1, 0xfd),
        Register('rwfe', 2, 0xfe),
        Register('rfe', 1, 0xfe),
        Register('rff', 1, 0xff),
        Register('rl100', 4, 0x100),
        Register('rw100', 2, 0x100),
        Register('r100', 1, 0x100),
        Register('r101', 1, 0x101),
        Register('rw102', 2, 0x102),
        Register('r102', 1, 0x102),
        Register('r103', 1, 0x103),
        Register('rl104', 4, 0x104),
        Register('rw104', 2, 0x104),
        Register('r104', 1, 0x104),
        Register('r105', 1, 0x105),
        Register('rw106', 2, 0x106),
        Register('r106', 1, 0x106),
        Register('r107', 1, 0x107),
        Register('rl108', 4, 0x108),
        Register('rw108', 2, 0x108),
        Register('r108', 1, 0x108),
        Register('r109', 1, 0x109),
        Register('rw10a', 2, 0x10a),
        Register('r10a', 1, 0x10a),
        Register('r10b', 1, 0x10b),
        Register('rl10c', 4, 0x10c),
        Register('rw10c', 2, 0x10c),
        Register('r10c', 1, 0x10c),
        Register('r10d', 1, 0x10d),
        Register('rw10e', 2, 0x10e),
        Register('r10e', 1, 0x10e),
        Register('r10f', 1, 0x10f),
        Register('rl110', 4, 0x110),
        Register('rw110', 2, 0x110),
        Register('r110', 1, 0x110),
        Register('r111', 1, 0x111),
        Register('rw112', 2, 0x112),
        Register('r112', 1, 0x112),
        Register('r113', 1, 0x113),
        Register('rl114', 4, 0x114),
        Register('rw114', 2, 0x114),
        Register('r114', 1, 0x114),
        Register('r115', 1, 0x115),
        Register('rw116', 2, 0x116),
        Register('r116', 1, 0x116),
        Register('r117', 1, 0x117),
        Register('rl118', 4, 0x118),
        Register('rw118', 2, 0x118),
        Register('r118', 1, 0x118),
        Register('r119', 1, 0x119),
        Register('rw11a', 2, 0x11a),
        Register('r11a', 1, 0x11a),
        Register('r11b', 1, 0x11b),
        Register('rl11c', 4, 0x11c),
        Register('rw11c', 2, 0x11c),
        Register('r11c', 1, 0x11c),
        Register('r11d', 1, 0x11d),
        Register('rw11e', 2, 0x11e),
        Register('r11e', 1, 0x11e),
        Register('r11f', 1, 0x11f),
        Register('rl120', 4, 0x120),
        Register('rw120', 2, 0x120),
        Register('r120', 1, 0x120),
        Register('r121', 1, 0x121),
        Register('rw122', 2, 0x122),
        Register('r122', 1, 0x122),
        Register('r123', 1, 0x123),
        Register('rl124', 4, 0x124),
        Register('rw124', 2, 0x124),
        Register('r124', 1, 0x124),
        Register('r125', 1, 0x125),
        Register('rw126', 2, 0x126),
        Register('r126', 1, 0x126),
        Register('r127', 1, 0x127),
        Register('rl128', 4, 0x128),
        Register('rw128', 2, 0x128),
        Register('r128', 1, 0x128),
        Register('r129', 1, 0x129),
        Register('rw12a', 2, 0x12a),
        Register('r12a', 1, 0x12a),
        Register('r12b', 1, 0x12b),
        Register('rl12c', 4, 0x12c),
        Register('rw12c', 2, 0x12c),
        Register('r12c', 1, 0x12c),
        Register('r12d', 1, 0x12d),
        Register('rw12e', 2, 0x12e),
        Register('r12e', 1, 0x12e),
        Register('r12f', 1, 0x12f),
        Register('rl130', 4, 0x130),
        Register('rw130', 2, 0x130),
        Register('r130', 1, 0x130),
        Register('r131', 1, 0x131),
        Register('rw132', 2, 0x132),
        Register('r132', 1, 0x132),
        Register('r133', 1, 0x133),
        Register('rl134', 4, 0x134),
        Register('rw134', 2, 0x134),
        Register('r134', 1, 0x134),
        Register('r135', 1, 0x135),
        Register('rw136', 2, 0x136),
        Register('r136', 1, 0x136),
        Register('r137', 1, 0x137),
        Register('rl138', 4, 0x138),
        Register('rw138', 2, 0x138),
        Register('r138', 1, 0x138),
        Register('r139', 1, 0x139),
        Register('rw13a', 2, 0x13a),
        Register('r13a', 1, 0x13a),
        Register('r13b', 1, 0x13b),
        Register('rl13c', 4, 0x13c),
        Register('rw13c', 2, 0x13c),
        Register('r13c', 1, 0x13c),
        Register('r13d', 1, 0x13d),
        Register('rw13e', 2, 0x13e),
        Register('r13e', 1, 0x13e),
        Register('r13f', 1, 0x13f),
        Register('rl140', 4, 0x140),
        Register('rw140', 2, 0x140),
        Register('r140', 1, 0x140),
        Register('r141', 1, 0x141),
        Register('rw142', 2, 0x142),
        Register('r142', 1, 0x142),
        Register('r143', 1, 0x143),
        Register('rl144', 4, 0x144),
        Register('rw144', 2, 0x144),
        Register('r144', 1, 0x144),
        Register('r145', 1, 0x145),
        Register('rw146', 2, 0x146),
        Register('r146', 1, 0x146),
        Register('r147', 1, 0x147),
        Register('rl148', 4, 0x148),
        Register('rw148', 2, 0x148),
        Register('r148', 1, 0x148),
        Register('r149', 1, 0x149),
        Register('rw14a', 2, 0x14a),
        Register('r14a', 1, 0x14a),
        Register('r14b', 1, 0x14b),
        Register('rl14c', 4, 0x14c),
        Register('rw14c', 2, 0x14c),
        Register('r14c', 1, 0x14c),
        Register('r14d', 1, 0x14d),
        Register('rw14e', 2, 0x14e),
        Register('r14e', 1, 0x14e),
        Register('r14f', 1, 0x14f),
        Register('rl150', 4, 0x150),
        Register('rw150', 2, 0x150),
        Register('r150', 1, 0x150),
        Register('r151', 1, 0x151),
        Register('rw152', 2, 0x152),
        Register('r152', 1, 0x152),
        Register('r153', 1, 0x153),
        Register('rl154', 4, 0x154),
        Register('rw154', 2, 0x154),
        Register('r154', 1, 0x154),
        Register('r155', 1, 0x155),
        Register('rw156', 2, 0x156),
        Register('r156', 1, 0x156),
        Register('r157', 1, 0x157),
        Register('rl158', 4, 0x158),
        Register('rw158', 2, 0x158),
        Register('r158', 1, 0x158),
        Register('r159', 1, 0x159),
        Register('rw15a', 2, 0x15a),
        Register('r15a', 1, 0x15a),
        Register('r15b', 1, 0x15b),
        Register('rl15c', 4, 0x15c),
        Register('rw15c', 2, 0x15c),
        Register('r15c', 1, 0x15c),
        Register('r15d', 1, 0x15d),
        Register('rw15e', 2, 0x15e),
        Register('r15e', 1, 0x15e),
        Register('r15f', 1, 0x15f),
        Register('rl160', 4, 0x160),
        Register('rw160', 2, 0x160),
        Register('r160', 1, 0x160),
        Register('r161', 1, 0x161),
        Register('rw162', 2, 0x162),
        Register('r162', 1, 0x162),
        Register('r163', 1, 0x163),
        Register('rl164', 4, 0x164),
        Register('rw164', 2, 0x164),
        Register('r164', 1, 0x164),
        Register('r165', 1, 0x165),
        Register('rw166', 2, 0x166),
        Register('r166', 1, 0x166),
        Register('r167', 1, 0x167),
        Register('rl168', 4, 0x168),
        Register('rw168', 2, 0x168),
        Register('r168', 1, 0x168),
        Register('r169', 1, 0x169),
        Register('rw16a', 2, 0x16a),
        Register('r16a', 1, 0x16a),
        Register('r16b', 1, 0x16b),
        Register('rl16c', 4, 0x16c),
        Register('rw16c', 2, 0x16c),
        Register('r16c', 1, 0x16c),
        Register('r16d', 1, 0x16d),
        Register('rw16e', 2, 0x16e),
        Register('r16e', 1, 0x16e),
        Register('r16f', 1, 0x16f),
        Register('rl170', 4, 0x170),
        Register('rw170', 2, 0x170),
        Register('r170', 1, 0x170),
        Register('r171', 1, 0x171),
        Register('rw172', 2, 0x172),
        Register('r172', 1, 0x172),
        Register('r173', 1, 0x173),
        Register('rl174', 4, 0x174),
        Register('rw174', 2, 0x174),
        Register('r174', 1, 0x174),
        Register('r175', 1, 0x175),
        Register('rw176', 2, 0x176),
        Register('r176', 1, 0x176),
        Register('r177', 1, 0x177),
        Register('rl178', 4, 0x178),
        Register('rw178', 2, 0x178),
        Register('r178', 1, 0x178),
        Register('r179', 1, 0x179),
        Register('rw17a', 2, 0x17a),
        Register('r17a', 1, 0x17a),
        Register('r17b', 1, 0x17b),
        Register('rl17c', 4, 0x17c),
        Register('rw17c', 2, 0x17c),
        Register('r17c', 1, 0x17c),
        Register('r17d', 1, 0x17d),
        Register('rw17e', 2, 0x17e),
        Register('r17e', 1, 0x17e),
        Register('r17f', 1, 0x17f),
        Register('rl180', 4, 0x180),
        Register('rw180', 2, 0x180),
        Register('r180', 1, 0x180),
        Register('r181', 1, 0x181),
        Register('rw182', 2, 0x182),
        Register('r182', 1, 0x182),
        Register('r183', 1, 0x183),
        Register('rl184', 4, 0x184),
        Register('rw184', 2, 0x184),
        Register('r184', 1, 0x184),
        Register('r185', 1, 0x185),
        Register('rw186', 2, 0x186),
        Register('r186', 1, 0x186),
        Register('r187', 1, 0x187),
        Register('rl188', 4, 0x188),
        Register('rw188', 2, 0x188),
        Register('r188', 1, 0x188),
        Register('r189', 1, 0x189),
        Register('rw18a', 2, 0x18a),
        Register('r18a', 1, 0x18a),
        Register('r18b', 1, 0x18b),
        Register('rl18c', 4, 0x18c),
        Register('rw18c', 2, 0x18c),
        Register('r18c', 1, 0x18c),
        Register('r18d', 1, 0x18d),
        Register('rw18e', 2, 0x18e),
        Register('r18e', 1, 0x18e),
        Register('r18f', 1, 0x18f),
        Register('rl190', 4, 0x190),
        Register('rw190', 2, 0x190),
        Register('r190', 1, 0x190),
        Register('r191', 1, 0x191),
        Register('rw192', 2, 0x192),
        Register('r192', 1, 0x192),
        Register('r193', 1, 0x193),
        Register('rl194', 4, 0x194),
        Register('rw194', 2, 0x194),
        Register('r194', 1, 0x194),
        Register('r195', 1, 0x195),
        Register('rw196', 2, 0x196),
        Register('r196', 1, 0x196),
        Register('r197', 1, 0x197),
        Register('rl198', 4, 0x198),
        Register('rw198', 2, 0x198),
        Register('r198', 1, 0x198),
        Register('r199', 1, 0x199),
        Register('rw19a', 2, 0x19a),
        Register('r19a', 1, 0x19a),
        Register('r19b', 1, 0x19b),
        Register('rl19c', 4, 0x19c),
        Register('rw19c', 2, 0x19c),
        Register('r19c', 1, 0x19c),
        Register('r19d', 1, 0x19d),
        Register('rw19e', 2, 0x19e),
        Register('r19e', 1, 0x19e),
        Register('r19f', 1, 0x19f),
        Register('rl1a0', 4, 0x1a0),
        Register('rw1a0', 2, 0x1a0),
        Register('r1a0', 1, 0x1a0),
        Register('r1a1', 1, 0x1a1),
        Register('rw1a2', 2, 0x1a2),
        Register('r1a2', 1, 0x1a2),
        Register('r1a3', 1, 0x1a3),
        Register('rl1a4', 4, 0x1a4),
        Register('rw1a4', 2, 0x1a4),
        Register('r1a4', 1, 0x1a4),
        Register('r1a5', 1, 0x1a5),
        Register('rw1a6', 2, 0x1a6),
        Register('r1a6', 1, 0x1a6),
        Register('r1a7', 1, 0x1a7),
        Register('rl1a8', 4, 0x1a8),
        Register('rw1a8', 2, 0x1a8),
        Register('r1a8', 1, 0x1a8),
        Register('r1a9', 1, 0x1a9),
        Register('rw1aa', 2, 0x1aa),
        Register('r1aa', 1, 0x1aa),
        Register('r1ab', 1, 0x1ab),
        Register('rl1ac', 4, 0x1ac),
        Register('rw1ac', 2, 0x1ac),
        Register('r1ac', 1, 0x1ac),
        Register('r1ad', 1, 0x1ad),
        Register('rw1ae', 2, 0x1ae),
        Register('r1ae', 1, 0x1ae),
        Register('r1af', 1, 0x1af),
        Register('rl1b0', 4, 0x1b0),
        Register('rw1b0', 2, 0x1b0),
        Register('r1b0', 1, 0x1b0),
        Register('r1b1', 1, 0x1b1),
        Register('rw1b2', 2, 0x1b2),
        Register('r1b2', 1, 0x1b2),
        Register('r1b3', 1, 0x1b3),
        Register('rl1b4', 4, 0x1b4),
        Register('rw1b4', 2, 0x1b4),
        Register('r1b4', 1, 0x1b4),
        Register('r1b5', 1, 0x1b5),
        Register('rw1b6', 2, 0x1b6),
        Register('r1b6', 1, 0x1b6),
        Register('r1b7', 1, 0x1b7),
        Register('rl1b8', 4, 0x1b8),
        Register('rw1b8', 2, 0x1b8),
        Register('r1b8', 1, 0x1b8),
        Register('r1b9', 1, 0x1b9),
        Register('rw1ba', 2, 0x1ba),
        Register('r1ba', 1, 0x1ba),
        Register('r1bb', 1, 0x1bb),
        Register('rl1bc', 4, 0x1bc),
        Register('rw1bc', 2, 0x1bc),
        Register('r1bc', 1, 0x1bc),
        Register('r1bd', 1, 0x1bd),
        Register('rw1be', 2, 0x1be),
        Register('r1be', 1, 0x1be),
        Register('r1bf', 1, 0x1bf),
        Register('rl1c0', 4, 0x1c0),
        Register('rw1c0', 2, 0x1c0),
        Register('r1c0', 1, 0x1c0),
        Register('r1c1', 1, 0x1c1),
        Register('rw1c2', 2, 0x1c2),
        Register('r1c2', 1, 0x1c2),
        Register('r1c3', 1, 0x1c3),
        Register('rl1c4', 4, 0x1c4),
        Register('rw1c4', 2, 0x1c4),
        Register('r1c4', 1, 0x1c4),
        Register('r1c5', 1, 0x1c5),
        Register('rw1c6', 2, 0x1c6),
        Register('r1c6', 1, 0x1c6),
        Register('r1c7', 1, 0x1c7),
        Register('rl1c8', 4, 0x1c8),
        Register('rw1c8', 2, 0x1c8),
        Register('r1c8', 1, 0x1c8),
        Register('r1c9', 1, 0x1c9),
        Register('rw1ca', 2, 0x1ca),
        Register('r1ca', 1, 0x1ca),
        Register('r1cb', 1, 0x1cb),
        Register('rl1cc', 4, 0x1cc),
        Register('rw1cc', 2, 0x1cc),
        Register('r1cc', 1, 0x1cc),
        Register('r1cd', 1, 0x1cd),
        Register('rw1ce', 2, 0x1ce),
        Register('r1ce', 1, 0x1ce),
        Register('r1cf', 1, 0x1cf),
        Register('rl1d0', 4, 0x1d0),
        Register('rw1d0', 2, 0x1d0),
        Register('r1d0', 1, 0x1d0),
        Register('r1d1', 1, 0x1d1),
        Register('rw1d2', 2, 0x1d2),
        Register('r1d2', 1, 0x1d2),
        Register('r1d3', 1, 0x1d3),
        Register('rl1d4', 4, 0x1d4),
        Register('rw1d4', 2, 0x1d4),
        Register('r1d4', 1, 0x1d4),
        Register('r1d5', 1, 0x1d5),
        Register('rw1d6', 2, 0x1d6),
        Register('r1d6', 1, 0x1d6),
        Register('r1d7', 1, 0x1d7),
        Register('rl1d8', 4, 0x1d8),
        Register('rw1d8', 2, 0x1d8),
        Register('r1d8', 1, 0x1d8),
        Register('r1d9', 1, 0x1d9),
        Register('rw1da', 2, 0x1da),
        Register('r1da', 1, 0x1da),
        Register('r1db', 1, 0x1db),
        Register('rl1dc', 4, 0x1dc),
        Register('rw1dc', 2, 0x1dc),
        Register('r1dc', 1, 0x1dc),
        Register('r1dd', 1, 0x1dd),
        Register('rw1de', 2, 0x1de),
        Register('r1de', 1, 0x1de),
        Register('r1df', 1, 0x1df),
        Register('rl1e0', 4, 0x1e0),
        Register('rw1e0', 2, 0x1e0),
        Register('r1e0', 1, 0x1e0),
        Register('r1e1', 1, 0x1e1),
        Register('rw1e2', 2, 0x1e2),
        Register('r1e2', 1, 0x1e2),
        Register('r1e3', 1, 0x1e3),
        Register('rl1e4', 4, 0x1e4),
        Register('rw1e4', 2, 0x1e4),
        Register('r1e4', 1, 0x1e4),
        Register('r1e5', 1, 0x1e5),
        Register('rw1e6', 2, 0x1e6),
        Register('r1e6', 1, 0x1e6),
        Register('r1e7', 1, 0x1e7),
        Register('rl1e8', 4, 0x1e8),
        Register('rw1e8', 2, 0x1e8),
        Register('r1e8', 1, 0x1e8),
        Register('r1e9', 1, 0x1e9),
        Register('rw1ea', 2, 0x1ea),
        Register('r1ea', 1, 0x1ea),
        Register('r1eb', 1, 0x1eb),
        Register('rl1ec', 4, 0x1ec),
        Register('rw1ec', 2, 0x1ec),
        Register('r1ec', 1, 0x1ec),
        Register('r1ed', 1, 0x1ed),
        Register('rw1ee', 2, 0x1ee),
        Register('r1ee', 1, 0x1ee),
        Register('r1ef', 1, 0x1ef),
        Register('rl1f0', 4, 0x1f0),
        Register('rw1f0', 2, 0x1f0),
        Register('r1f0', 1, 0x1f0),
        Register('r1f1', 1, 0x1f1),
        Register('rw1f2', 2, 0x1f2),
        Register('r1f2', 1, 0x1f2),
        Register('r1f3', 1, 0x1f3),
        Register('rl1f4', 4, 0x1f4),
        Register('rw1f4', 2, 0x1f4),
        Register('r1f4', 1, 0x1f4),
        Register('r1f5', 1, 0x1f5),
        Register('rw1f6', 2, 0x1f6),
        Register('r1f6', 1, 0x1f6),
        Register('r1f7', 1, 0x1f7),
        Register('rl1f8', 4, 0x1f8),
        Register('rw1f8', 2, 0x1f8),
        Register('r1f8', 1, 0x1f8),
        Register('r1f9', 1, 0x1f9),
        Register('rw1fa', 2, 0x1fa),
        Register('r1fa', 1, 0x1fa),
        Register('r1fb', 1, 0x1fb),
        Register('rl1fc', 4, 0x1fc),
        Register('rw1fc', 2, 0x1fc),
        Register('r1fc', 1, 0x1fc),
        Register('r1fd', 1, 0x1fd),
        Register('rw1fe', 2, 0x1fe),
        Register('r1fe', 1, 0x1fe),
        Register('r1ff', 1, 0x1ff),
        Register('psw', 2, 0x0),
        Register('pc', 2, 0x10, alias_names=('ip',)),
        Register('sp', 2, 0x18)
    ]

register_arch(['mcs96:le:16:default'], 16, Endness.LE, ArchPcode_MCS96_LE_16_default)
