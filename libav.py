'''
https://stackoverflow.com/questions/7586504/python-accessing-dll-using-ctypes
https://msdn.microsoft.com/en-us/library/784bt7z7.aspx
https://stackoverflow.com/questions/2980479/python-ctypes-loading-dll-from-from-a-relative-path
https://github.com/sydhds/Avpy/blob/master/avpy/version/av9.py
https://stackoverflow.com/questions/43810423/what-is-the-most-efficient-way-to-copy-an-externally-provided-buffer-to-bytes
'''
from ctypes import *
'''
avcodec-58
'''

#avcodec.h
from enum import Enum, auto
class AVCodecID(Enum):
    AV_CODEC_ID_NONE					=0

    # video codecs */
    AV_CODEC_ID_MPEG1VIDEO					=auto()
    AV_CODEC_ID_MPEG2VIDEO					=auto() #/< preferred ID for MPEG-1/2 video decoding
    AV_CODEC_ID_H261					=auto()
    AV_CODEC_ID_H263					=auto()
    AV_CODEC_ID_RV10					=auto()
    AV_CODEC_ID_RV20					=auto()
    AV_CODEC_ID_MJPEG					=auto()
    AV_CODEC_ID_MJPEGB					=auto()
    AV_CODEC_ID_LJPEG					=auto()
    AV_CODEC_ID_SP5X					=auto()
    AV_CODEC_ID_JPEGLS					=auto()
    AV_CODEC_ID_MPEG4					=auto()
    AV_CODEC_ID_RAWVIDEO					=auto()
    AV_CODEC_ID_MSMPEG4V1					=auto()
    AV_CODEC_ID_MSMPEG4V2					=auto()
    AV_CODEC_ID_MSMPEG4V3					=auto()
    AV_CODEC_ID_WMV1					=auto()
    AV_CODEC_ID_WMV2					=auto()
    AV_CODEC_ID_H263P					=auto()
    AV_CODEC_ID_H263I					=auto()
    AV_CODEC_ID_FLV1					=auto()
    AV_CODEC_ID_SVQ1					=auto()
    AV_CODEC_ID_SVQ3					=auto()
    AV_CODEC_ID_DVVIDEO					=auto()
    AV_CODEC_ID_HUFFYUV					=auto()
    AV_CODEC_ID_CYUV					=auto()
    AV_CODEC_ID_H264					=auto()
    AV_CODEC_ID_INDEO3					=auto()
    AV_CODEC_ID_VP3					=auto()
    AV_CODEC_ID_THEORA					=auto()
    AV_CODEC_ID_ASV1					=auto()
    AV_CODEC_ID_ASV2					=auto()
    AV_CODEC_ID_FFV1					=auto()
    AV_CODEC_ID_4XM					=auto()
    AV_CODEC_ID_VCR1					=auto()
    AV_CODEC_ID_CLJR					=auto()
    AV_CODEC_ID_MDEC					=auto()
    AV_CODEC_ID_ROQ					=auto()
    AV_CODEC_ID_INTERPLAY_VIDEO					=auto()
    AV_CODEC_ID_XAN_WC3					=auto()
    AV_CODEC_ID_XAN_WC4					=auto()
    AV_CODEC_ID_RPZA					=auto()
    AV_CODEC_ID_CINEPAK					=auto()
    AV_CODEC_ID_WS_VQA					=auto()
    AV_CODEC_ID_MSRLE					=auto()
    AV_CODEC_ID_MSVIDEO1					=auto()
    AV_CODEC_ID_IDCIN					=auto()
    AV_CODEC_ID_8BPS					=auto()
    AV_CODEC_ID_SMC					=auto()
    AV_CODEC_ID_FLIC					=auto()
    AV_CODEC_ID_TRUEMOTION1					=auto()
    AV_CODEC_ID_VMDVIDEO					=auto()
    AV_CODEC_ID_MSZH					=auto()
    AV_CODEC_ID_ZLIB					=auto()
    AV_CODEC_ID_QTRLE					=auto()
    AV_CODEC_ID_TSCC					=auto()
    AV_CODEC_ID_ULTI					=auto()
    AV_CODEC_ID_QDRAW					=auto()
    AV_CODEC_ID_VIXL					=auto()
    AV_CODEC_ID_QPEG					=auto()
    AV_CODEC_ID_PNG					=auto()
    AV_CODEC_ID_PPM					=auto()
    AV_CODEC_ID_PBM					=auto()
    AV_CODEC_ID_PGM					=auto()
    AV_CODEC_ID_PGMYUV					=auto()
    AV_CODEC_ID_PAM					=auto()
    AV_CODEC_ID_FFVHUFF					=auto()
    AV_CODEC_ID_RV30					=auto()
    AV_CODEC_ID_RV40					=auto()
    AV_CODEC_ID_VC1					=auto()
    AV_CODEC_ID_WMV3					=auto()
    AV_CODEC_ID_LOCO					=auto()
    AV_CODEC_ID_WNV1					=auto()
    AV_CODEC_ID_AASC					=auto()
    AV_CODEC_ID_INDEO2					=auto()
    AV_CODEC_ID_FRAPS					=auto()
    AV_CODEC_ID_TRUEMOTION2					=auto()
    AV_CODEC_ID_BMP					=auto()
    AV_CODEC_ID_CSCD					=auto()
    AV_CODEC_ID_MMVIDEO					=auto()
    AV_CODEC_ID_ZMBV					=auto()
    AV_CODEC_ID_AVS					=auto()
    AV_CODEC_ID_SMACKVIDEO					=auto()
    AV_CODEC_ID_NUV					=auto()
    AV_CODEC_ID_KMVC					=auto()
    AV_CODEC_ID_FLASHSV					=auto()
    AV_CODEC_ID_CAVS					=auto()
    AV_CODEC_ID_JPEG2000					=auto()
    AV_CODEC_ID_VMNC					=auto()
    AV_CODEC_ID_VP5					=auto()
    AV_CODEC_ID_VP6					=auto()
    AV_CODEC_ID_VP6F					=auto()
    AV_CODEC_ID_TARGA					=auto()
    AV_CODEC_ID_DSICINVIDEO					=auto()
    AV_CODEC_ID_TIERTEXSEQVIDEO					=auto()
    AV_CODEC_ID_TIFF					=auto()
    AV_CODEC_ID_GIF					=auto()
    AV_CODEC_ID_DXA					=auto()
    AV_CODEC_ID_DNXHD					=auto()
    AV_CODEC_ID_THP					=auto()
    AV_CODEC_ID_SGI					=auto()
    AV_CODEC_ID_C93					=auto()
    AV_CODEC_ID_BETHSOFTVID					=auto()
    AV_CODEC_ID_PTX					=auto()
    AV_CODEC_ID_TXD					=auto()
    AV_CODEC_ID_VP6A					=auto()
    AV_CODEC_ID_AMV					=auto()
    AV_CODEC_ID_VB					=auto()
    AV_CODEC_ID_PCX					=auto()
    AV_CODEC_ID_SUNRAST					=auto()
    AV_CODEC_ID_INDEO4					=auto()
    AV_CODEC_ID_INDEO5					=auto()
    AV_CODEC_ID_MIMIC					=auto()
    AV_CODEC_ID_RL2					=auto()
    AV_CODEC_ID_ESCAPE124					=auto()
    AV_CODEC_ID_DIRAC					=auto()
    AV_CODEC_ID_BFI					=auto()
    AV_CODEC_ID_CMV					=auto()
    AV_CODEC_ID_MOTIONPIXELS					=auto()
    AV_CODEC_ID_TGV					=auto()
    AV_CODEC_ID_TGQ					=auto()
    AV_CODEC_ID_TQI					=auto()
    AV_CODEC_ID_AURA					=auto()
    AV_CODEC_ID_AURA2					=auto()
    AV_CODEC_ID_V210X					=auto()
    AV_CODEC_ID_TMV					=auto()
    AV_CODEC_ID_V210					=auto()
    AV_CODEC_ID_DPX					=auto()
    AV_CODEC_ID_MAD					=auto()
    AV_CODEC_ID_FRWU					=auto()
    AV_CODEC_ID_FLASHSV2					=auto()
    AV_CODEC_ID_CDGRAPHICS					=auto()
    AV_CODEC_ID_R210					=auto()
    AV_CODEC_ID_ANM					=auto()
    AV_CODEC_ID_BINKVIDEO					=auto()
    AV_CODEC_ID_IFF_ILBM					=auto()
#define AV_CODEC_ID_IFF_BYTERUN1 AV_CODEC_ID_IFF_ILBM
    AV_CODEC_ID_KGV1					=auto()
    AV_CODEC_ID_YOP					=auto()
    AV_CODEC_ID_VP8					=auto()
    AV_CODEC_ID_PICTOR					=auto()
    AV_CODEC_ID_ANSI					=auto()
    AV_CODEC_ID_A64_MULTI					=auto()
    AV_CODEC_ID_A64_MULTI5					=auto()
    AV_CODEC_ID_R10K					=auto()
    AV_CODEC_ID_MXPEG					=auto()
    AV_CODEC_ID_LAGARITH					=auto()
    AV_CODEC_ID_PRORES					=auto()
    AV_CODEC_ID_JV					=auto()
    AV_CODEC_ID_DFA					=auto()
    AV_CODEC_ID_WMV3IMAGE					=auto()
    AV_CODEC_ID_VC1IMAGE					=auto()
    AV_CODEC_ID_UTVIDEO					=auto()
    AV_CODEC_ID_BMV_VIDEO					=auto()
    AV_CODEC_ID_VBLE					=auto()
    AV_CODEC_ID_DXTORY					=auto()
    AV_CODEC_ID_V410					=auto()
    AV_CODEC_ID_XWD					=auto()
    AV_CODEC_ID_CDXL					=auto()
    AV_CODEC_ID_XBM					=auto()
    AV_CODEC_ID_ZEROCODEC					=auto()
    AV_CODEC_ID_MSS1					=auto()
    AV_CODEC_ID_MSA1					=auto()
    AV_CODEC_ID_TSCC2					=auto()
    AV_CODEC_ID_MTS2					=auto()
    AV_CODEC_ID_CLLC					=auto()
    AV_CODEC_ID_MSS2					=auto()
    AV_CODEC_ID_VP9					=auto()
    AV_CODEC_ID_AIC					=auto()
    AV_CODEC_ID_ESCAPE130					=auto()
    AV_CODEC_ID_G2M					=auto()
    AV_CODEC_ID_WEBP					=auto()
    AV_CODEC_ID_HNM4_VIDEO					=auto()
    AV_CODEC_ID_HEVC					=auto()
#define AV_CODEC_ID_H265 AV_CODEC_ID_HEVC
    AV_CODEC_ID_FIC					=auto()
    AV_CODEC_ID_ALIAS_PIX					=auto()
    AV_CODEC_ID_BRENDER_PIX					=auto()
    AV_CODEC_ID_PAF_VIDEO					=auto()
    AV_CODEC_ID_EXR					=auto()
    AV_CODEC_ID_VP7					=auto()
    AV_CODEC_ID_SANM					=auto()
    AV_CODEC_ID_SGIRLE					=auto()
    AV_CODEC_ID_MVC1					=auto()
    AV_CODEC_ID_MVC2					=auto()
    AV_CODEC_ID_HQX					=auto()
    AV_CODEC_ID_TDSC					=auto()
    AV_CODEC_ID_HQ_HQA					=auto()
    AV_CODEC_ID_HAP					=auto()
    AV_CODEC_ID_DDS					=auto()
    AV_CODEC_ID_DXV					=auto()
    AV_CODEC_ID_SCREENPRESSO					=auto()
    AV_CODEC_ID_RSCC					=auto()

    AV_CODEC_ID_Y41P = 0x8000
    AV_CODEC_ID_AVRP					=auto()
    AV_CODEC_ID_012V					=auto()
    AV_CODEC_ID_AVUI					=auto()
    AV_CODEC_ID_AYUV					=auto()
    AV_CODEC_ID_TARGA_Y216					=auto()
    AV_CODEC_ID_V308					=auto()
    AV_CODEC_ID_V408					=auto()
    AV_CODEC_ID_YUV4					=auto()
    AV_CODEC_ID_AVRN					=auto()
    AV_CODEC_ID_CPIA					=auto()
    AV_CODEC_ID_XFACE					=auto()
    AV_CODEC_ID_SNOW					=auto()
    AV_CODEC_ID_SMVJPEG					=auto()
    AV_CODEC_ID_APNG					=auto()
    AV_CODEC_ID_DAALA					=auto()
    AV_CODEC_ID_CFHD					=auto()
    AV_CODEC_ID_TRUEMOTION2RT					=auto()
    AV_CODEC_ID_M101					=auto()
    AV_CODEC_ID_MAGICYUV					=auto()
    AV_CODEC_ID_SHEERVIDEO					=auto()
    AV_CODEC_ID_YLC					=auto()
    AV_CODEC_ID_PSD					=auto()
    AV_CODEC_ID_PIXLET					=auto()
    AV_CODEC_ID_SPEEDHQ					=auto()
    AV_CODEC_ID_FMVC					=auto()
    AV_CODEC_ID_SCPR					=auto()
    AV_CODEC_ID_CLEARVIDEO					=auto()
    AV_CODEC_ID_XPM					=auto()
    AV_CODEC_ID_AV1					=auto()
    AV_CODEC_ID_BITPACKED					=auto()
    AV_CODEC_ID_MSCC					=auto()
    AV_CODEC_ID_SRGC					=auto()
    AV_CODEC_ID_SVG					=auto()
    AV_CODEC_ID_GDV					=auto()
    AV_CODEC_ID_FITS					=auto()

    # various PCM "codecs" */
    AV_CODEC_ID_FIRST_AUDIO = 0x10000     #/< A dummy id pointing at the start of audio codecs
    AV_CODEC_ID_PCM_S16LE = 0x10000
    AV_CODEC_ID_PCM_S16BE					=auto()
    AV_CODEC_ID_PCM_U16LE					=auto()
    AV_CODEC_ID_PCM_U16BE					=auto()
    AV_CODEC_ID_PCM_S8					=auto()
    AV_CODEC_ID_PCM_U8					=auto()
    AV_CODEC_ID_PCM_MULAW					=auto()
    AV_CODEC_ID_PCM_ALAW					=auto()
    AV_CODEC_ID_PCM_S32LE					=auto()
    AV_CODEC_ID_PCM_S32BE					=auto()
    AV_CODEC_ID_PCM_U32LE					=auto()
    AV_CODEC_ID_PCM_U32BE					=auto()
    AV_CODEC_ID_PCM_S24LE					=auto()
    AV_CODEC_ID_PCM_S24BE					=auto()
    AV_CODEC_ID_PCM_U24LE					=auto()
    AV_CODEC_ID_PCM_U24BE					=auto()
    AV_CODEC_ID_PCM_S24DAUD					=auto()
    AV_CODEC_ID_PCM_ZORK					=auto()
    AV_CODEC_ID_PCM_S16LE_PLANAR					=auto()
    AV_CODEC_ID_PCM_DVD					=auto()
    AV_CODEC_ID_PCM_F32BE					=auto()
    AV_CODEC_ID_PCM_F32LE					=auto()
    AV_CODEC_ID_PCM_F64BE					=auto()
    AV_CODEC_ID_PCM_F64LE					=auto()
    AV_CODEC_ID_PCM_BLURAY					=auto()
    AV_CODEC_ID_PCM_LXF					=auto()
    AV_CODEC_ID_S302M					=auto()
    AV_CODEC_ID_PCM_S8_PLANAR					=auto()
    AV_CODEC_ID_PCM_S24LE_PLANAR					=auto()
    AV_CODEC_ID_PCM_S32LE_PLANAR					=auto()
    AV_CODEC_ID_PCM_S16BE_PLANAR					=auto()

    AV_CODEC_ID_PCM_S64LE = 0x10800
    AV_CODEC_ID_PCM_S64BE					=auto()
    AV_CODEC_ID_PCM_F16LE					=auto()
    AV_CODEC_ID_PCM_F24LE					=auto()

    # various ADPCM codecs */
    AV_CODEC_ID_ADPCM_IMA_QT = 0x11000
    AV_CODEC_ID_ADPCM_IMA_WAV					=auto()
    AV_CODEC_ID_ADPCM_IMA_DK3					=auto()
    AV_CODEC_ID_ADPCM_IMA_DK4					=auto()
    AV_CODEC_ID_ADPCM_IMA_WS					=auto()
    AV_CODEC_ID_ADPCM_IMA_SMJPEG					=auto()
    AV_CODEC_ID_ADPCM_MS					=auto()
    AV_CODEC_ID_ADPCM_4XM					=auto()
    AV_CODEC_ID_ADPCM_XA					=auto()
    AV_CODEC_ID_ADPCM_ADX					=auto()
    AV_CODEC_ID_ADPCM_EA					=auto()
    AV_CODEC_ID_ADPCM_G726					=auto()
    AV_CODEC_ID_ADPCM_CT					=auto()
    AV_CODEC_ID_ADPCM_SWF					=auto()
    AV_CODEC_ID_ADPCM_YAMAHA					=auto()
    AV_CODEC_ID_ADPCM_SBPRO_4					=auto()
    AV_CODEC_ID_ADPCM_SBPRO_3					=auto()
    AV_CODEC_ID_ADPCM_SBPRO_2					=auto()
    AV_CODEC_ID_ADPCM_THP					=auto()
    AV_CODEC_ID_ADPCM_IMA_AMV					=auto()
    AV_CODEC_ID_ADPCM_EA_R1					=auto()
    AV_CODEC_ID_ADPCM_EA_R3					=auto()
    AV_CODEC_ID_ADPCM_EA_R2					=auto()
    AV_CODEC_ID_ADPCM_IMA_EA_SEAD					=auto()
    AV_CODEC_ID_ADPCM_IMA_EA_EACS					=auto()
    AV_CODEC_ID_ADPCM_EA_XAS					=auto()
    AV_CODEC_ID_ADPCM_EA_MAXIS_XA					=auto()
    AV_CODEC_ID_ADPCM_IMA_ISS					=auto()
    AV_CODEC_ID_ADPCM_G722					=auto()
    AV_CODEC_ID_ADPCM_IMA_APC					=auto()
    AV_CODEC_ID_ADPCM_VIMA					=auto()

    AV_CODEC_ID_ADPCM_AFC = 0x11800
    AV_CODEC_ID_ADPCM_IMA_OKI					=auto()
    AV_CODEC_ID_ADPCM_DTK					=auto()
    AV_CODEC_ID_ADPCM_IMA_RAD					=auto()
    AV_CODEC_ID_ADPCM_G726LE					=auto()
    AV_CODEC_ID_ADPCM_THP_LE					=auto()
    AV_CODEC_ID_ADPCM_PSX					=auto()
    AV_CODEC_ID_ADPCM_AICA					=auto()
    AV_CODEC_ID_ADPCM_IMA_DAT4					=auto()
    AV_CODEC_ID_ADPCM_MTAF					=auto()

    # AMR */
    AV_CODEC_ID_AMR_NB = 0x12000
    AV_CODEC_ID_AMR_WB					=auto()

    # RealAudio codecs*/
    AV_CODEC_ID_RA_144 = 0x13000
    AV_CODEC_ID_RA_288					=auto()

    # various DPCM codecs */
    AV_CODEC_ID_ROQ_DPCM = 0x14000
    AV_CODEC_ID_INTERPLAY_DPCM					=auto()
    AV_CODEC_ID_XAN_DPCM					=auto()
    AV_CODEC_ID_SOL_DPCM					=auto()

    AV_CODEC_ID_SDX2_DPCM = 0x14800
    AV_CODEC_ID_GREMLIN_DPCM					=auto()

    # audio codecs */
    AV_CODEC_ID_MP2 = 0x15000
    AV_CODEC_ID_MP3					=auto() #/< preferred ID for decoding MPEG audio layer 1, 2 or 3
    AV_CODEC_ID_AAC					=auto()
    AV_CODEC_ID_AC3					=auto()
    AV_CODEC_ID_DTS					=auto()
    AV_CODEC_ID_VORBIS					=auto()
    AV_CODEC_ID_DVAUDIO					=auto()
    AV_CODEC_ID_WMAV1					=auto()
    AV_CODEC_ID_WMAV2					=auto()
    AV_CODEC_ID_MACE3					=auto()
    AV_CODEC_ID_MACE6					=auto()
    AV_CODEC_ID_VMDAUDIO					=auto()
    AV_CODEC_ID_FLAC					=auto()
    AV_CODEC_ID_MP3ADU					=auto()
    AV_CODEC_ID_MP3ON4					=auto()
    AV_CODEC_ID_SHORTEN					=auto()
    AV_CODEC_ID_ALAC					=auto()
    AV_CODEC_ID_WESTWOOD_SND1					=auto()
    AV_CODEC_ID_GSM					=auto() #/< as in Berlin toast format
    AV_CODEC_ID_QDM2					=auto()
    AV_CODEC_ID_COOK					=auto()
    AV_CODEC_ID_TRUESPEECH					=auto()
    AV_CODEC_ID_TTA					=auto()
    AV_CODEC_ID_SMACKAUDIO					=auto()
    AV_CODEC_ID_QCELP					=auto()
    AV_CODEC_ID_WAVPACK					=auto()
    AV_CODEC_ID_DSICINAUDIO					=auto()
    AV_CODEC_ID_IMC					=auto()
    AV_CODEC_ID_MUSEPACK7					=auto()
    AV_CODEC_ID_MLP					=auto()
    AV_CODEC_ID_GSM_MS					=auto() # as found in WAV */
    AV_CODEC_ID_ATRAC3					=auto()
    AV_CODEC_ID_APE					=auto()
    AV_CODEC_ID_NELLYMOSER					=auto()
    AV_CODEC_ID_MUSEPACK8					=auto()
    AV_CODEC_ID_SPEEX					=auto()
    AV_CODEC_ID_WMAVOICE					=auto()
    AV_CODEC_ID_WMAPRO					=auto()
    AV_CODEC_ID_WMALOSSLESS					=auto()
    AV_CODEC_ID_ATRAC3P					=auto()
    AV_CODEC_ID_EAC3					=auto()
    AV_CODEC_ID_SIPR					=auto()
    AV_CODEC_ID_MP1					=auto()
    AV_CODEC_ID_TWINVQ					=auto()
    AV_CODEC_ID_TRUEHD					=auto()
    AV_CODEC_ID_MP4ALS					=auto()
    AV_CODEC_ID_ATRAC1					=auto()
    AV_CODEC_ID_BINKAUDIO_RDFT					=auto()
    AV_CODEC_ID_BINKAUDIO_DCT					=auto()
    AV_CODEC_ID_AAC_LATM					=auto()
    AV_CODEC_ID_QDMC					=auto()
    AV_CODEC_ID_CELT					=auto()
    AV_CODEC_ID_G723_1					=auto()
    AV_CODEC_ID_G729					=auto()
    AV_CODEC_ID_8SVX_EXP					=auto()
    AV_CODEC_ID_8SVX_FIB					=auto()
    AV_CODEC_ID_BMV_AUDIO					=auto()
    AV_CODEC_ID_RALF					=auto()
    AV_CODEC_ID_IAC					=auto()
    AV_CODEC_ID_ILBC					=auto()
    AV_CODEC_ID_OPUS					=auto()
    AV_CODEC_ID_COMFORT_NOISE					=auto()
    AV_CODEC_ID_TAK					=auto()
    AV_CODEC_ID_METASOUND					=auto()
    AV_CODEC_ID_PAF_AUDIO					=auto()
    AV_CODEC_ID_ON2AVC					=auto()
    AV_CODEC_ID_DSS_SP					=auto()
    AV_CODEC_ID_CODEC2					=auto()

    AV_CODEC_ID_FFWAVESYNTH = 0x15800
    AV_CODEC_ID_SONIC					=auto()
    AV_CODEC_ID_SONIC_LS					=auto()
    AV_CODEC_ID_EVRC					=auto()
    AV_CODEC_ID_SMV					=auto()
    AV_CODEC_ID_DSD_LSBF					=auto()
    AV_CODEC_ID_DSD_MSBF					=auto()
    AV_CODEC_ID_DSD_LSBF_PLANAR					=auto()
    AV_CODEC_ID_DSD_MSBF_PLANAR					=auto()
    AV_CODEC_ID_4GV					=auto()
    AV_CODEC_ID_INTERPLAY_ACM					=auto()
    AV_CODEC_ID_XMA1					=auto()
    AV_CODEC_ID_XMA2					=auto()
    AV_CODEC_ID_DST					=auto()
    AV_CODEC_ID_ATRAC3AL					=auto()
    AV_CODEC_ID_ATRAC3PAL					=auto()
    AV_CODEC_ID_DOLBY_E					=auto()
    AV_CODEC_ID_APTX					=auto()
    AV_CODEC_ID_APTX_HD					=auto()
    AV_CODEC_ID_SBC					=auto()

    # subtitle codecs */
    AV_CODEC_ID_FIRST_SUBTITLE = 0x17000         #/< A dummy ID pointing at the start of subtitle codecs.
    AV_CODEC_ID_DVD_SUBTITLE = 0x17000
    AV_CODEC_ID_DVB_SUBTITLE					=auto()
    AV_CODEC_ID_TEXT					=auto()  #/< raw UTF-8 text
    AV_CODEC_ID_XSUB					=auto()
    AV_CODEC_ID_SSA					=auto()
    AV_CODEC_ID_MOV_TEXT					=auto()
    AV_CODEC_ID_HDMV_PGS_SUBTITLE					=auto()
    AV_CODEC_ID_DVB_TELETEXT					=auto()
    AV_CODEC_ID_SRT					=auto()

    AV_CODEC_ID_MICRODVD   = 0x17800
    AV_CODEC_ID_EIA_608					=auto()
    AV_CODEC_ID_JACOSUB					=auto()
    AV_CODEC_ID_SAMI					=auto()
    AV_CODEC_ID_REALTEXT					=auto()
    AV_CODEC_ID_STL					=auto()
    AV_CODEC_ID_SUBVIEWER1					=auto()
    AV_CODEC_ID_SUBVIEWER					=auto()
    AV_CODEC_ID_SUBRIP					=auto()
    AV_CODEC_ID_WEBVTT					=auto()
    AV_CODEC_ID_MPL2					=auto()
    AV_CODEC_ID_VPLAYER					=auto()
    AV_CODEC_ID_PJS					=auto()
    AV_CODEC_ID_ASS					=auto()
    AV_CODEC_ID_HDMV_TEXT_SUBTITLE					=auto()
    AV_CODEC_ID_TTML					=auto()

    # other specific kind of codecs (generally used for attachments) */
    AV_CODEC_ID_FIRST_UNKNOWN = 0x18000           #/< A dummy ID pointing at the start of various fake codecs.
    AV_CODEC_ID_TTF = 0x18000

    AV_CODEC_ID_SCTE_35					=auto() #/< Contain timestamp estimated through PCR of program stream.
    AV_CODEC_ID_BINTEXT    = 0x18800
    AV_CODEC_ID_XBIN					=auto()
    AV_CODEC_ID_IDF					=auto()
    AV_CODEC_ID_OTF					=auto()
    AV_CODEC_ID_SMPTE_KLV					=auto()
    AV_CODEC_ID_DVD_NAV					=auto()
    AV_CODEC_ID_TIMED_ID3					=auto()
    AV_CODEC_ID_BIN_DATA					=auto()


    AV_CODEC_ID_PROBE = 0x19000 #/< codec_id is not known (like AV_CODEC_ID_NONE) but lavf should attempt to identify it

    AV_CODEC_ID_MPEG2TS = 0x20000 #*< _FAKE_ codec to indicate a raw MPEG-2 TS
                                #* stream (only used by libavformat) */
    AV_CODEC_ID_MPEG4SYSTEMS = 0x20001 #*< _FAKE_ codec to indicate a MPEG-4 Systems
                                #* stream (only used by libavformat) */
    AV_CODEC_ID_FFMETADATA = 0x21000   #/< Dummy codec for streams containing only metadata information.
    AV_CODEC_ID_WRAPPED_AVFRAME = 0x21001 #/< Passthrough codec, AVFrames wrapped in AVPacket
'''
'''

import ctypes
from ctypes.wintypes import *
ULONG_PTR = ctypes.POINTER(DWORD)
class AVProfile(ctypes.Structure):#avcodec.h
    pass
class AVRational(ctypes.Structure): #rational.h
    pass
class AVClass(ctypes.Structure): #log.h
    pass
class AVCodecDescriptor(ctypes.Structure): #avcodec.h 
    pass
class RcOverride(ctypes.Structure): #avcodec.h
    pass
class AVBufferRef(ctypes.Structure): #buffer.h
    pass
class AVHWAccel(ctypes.Structure): #avcodec.h
    pass
class AVCodecDefault(ctypes.Structure):
    pass
class AVSubtitle(ctypes.Structure): #avcodec.h 
    pass
class AVPacket(ctypes.Structure): #avcodec.h 
    pass
class AVFrame(ctypes.Structure): #frame.h
    pass
class AVCodecHWConfigInternal(ctypes.Structure):
    pass
class AVCodec(ctypes.Structure): #avcodec.h
    pass    
class AVCodecContext(ctypes.Structure): #avcodec.h
    pass
class AVCodecInternal(ctypes.Structure):
    pass
class AVFrameSideData(ctypes.Structure): #frame.h
    pass
class AVDictionary(ctypes.Structure): #dict.h
    pass
class AVBuffer(ctypes.Structure): #dict.h
    pass
class AVCodecParserContext(ctypes.Structure): #avcodec.h
    pass
class AVCodecParser(ctypes.Structure): #avcodec.h
    pass
class AVInputFormat(ctypes.Structure): #avformat.h
    pass
class AVOutputFormat(ctypes.Structure): #avformat.h
    pass
class AVStream(ctypes.Structure): #avformat.h
    pass
class AVProgram(ctypes.Structure): #avformat.h
    pass
class AVChapter(ctypes.Structure): #avformat.h
    pass
class AVIOContext(ctypes.Structure): #avio.h
    pass
class AVIOInterruptCB(ctypes.Structure): #avio.h
    pass
class AVFormatInternal(ctypes.Structure):
    pass
class AVFormatContext(ctypes.Structure): #avformat.h
    pass
class AVPacketSideData(ctypes.Structure):
    pass
class AVCodecParameters(ctypes.Structure): #avcodec.h 
    pass
class AVStreamInfo(ctypes.Structure):
    pass    
class AVPacketList(ctypes.Structure):
    pass    
class AVProbeData(ctypes.Structure):
    pass    
class AVIndexEntry(ctypes.Structure):
    pass    
class AVStreamInternal(ctypes.Structure):
    pass    
class AVPicture(ctypes.Structure): #avcodec.h 
    pass
class AVRational(ctypes.Structure): #rational.h
    _fields_=(('num',c_int),
              ('den',c_int))

AV_NUM_DATA_POINTERS=8 #frame.h
AV_INPUT_BUFFER_PADDING_SIZE=64 #avcodec.h

class AVFrame(ctypes.Structure): #frame.h
    _fields_ = (('data',POINTER(c_uint8)*AV_NUM_DATA_POINTERS), #uint8_t *data[AV_NUM_DATA_POINTERS];
                ('linesize',c_int*AV_NUM_DATA_POINTERS),
                ('extended_data',POINTER(POINTER(c_uint8))),
                ('width', c_int),
                ('height', c_int),
                ('nb_samples', c_int),
                ('format', c_int),
                ('key_frame', c_int),
                ('pict_type', c_int), #enum AVPictureType
                ('sample_aspect_ratio', AVRational),
                ('pts', c_int64),
                ('pkt_pts', c_int64),
                ('pkt_dts', c_int64),
                ('coded_picture_number', c_int),
                ('display_picture_number', c_int),
                ('quality', c_int),
                ('opaque', c_void_p),
                ('error', c_uint64*AV_NUM_DATA_POINTERS),
                ('repeat_pict', c_int),
                ('interlaced_frame', c_int),
                ('top_field_first', c_int),
                ('palette_has_changed', c_int),
                ('reordered_opaque', c_int64),
                ('sample_rate', c_int),
                ('channel_layout', c_uint64),
                ('buf', POINTER(AVBufferRef)*AV_NUM_DATA_POINTERS), #AVBufferRef *buf[AV_NUM_DATA_POINTERS];
                ('extended_buf', POINTER(POINTER(AVBufferRef))), 
                ('nb_extended_buf', c_int),
                ('side_data', POINTER(POINTER(AVFrameSideData))),
                ('nb_side_data', c_int),
                ('flags', c_int),
                ('color_range', c_int), #enum AVColorRange
                ('color_primaries', c_int), #enum AVColorPrimaries
                ('color_trc', c_int), #enum AVColorTransferCharacteristic
                ('colorspace', c_int), #enum AVColorSpace
                ('chroma_location', c_int), #enum AVChromaLocation
                ('best_effort_timestamp', c_int64),
                ('pkt_pos', c_int64),
                ('pkt_duration', c_int64),
                ('metadata', POINTER(AVDictionary)),
                ('decode_error_flags', c_int),
                ('channels', c_int),
                ('pkt_size', c_int),
                ('qscale_table', POINTER(c_int8)),
                ('qstride', c_int),
                ('qscale_type', c_int),
                ('qp_table_buf', POINTER(AVBufferRef)),
                ('hw_frames_ctx', POINTER(AVBufferRef)),
                ('opaque_ref', POINTER(AVBufferRef)),
                ('crop_top'   ,c_size_t),
                ('crop_bottom',c_size_t),
                ('crop_left'  ,c_size_t),
                ('crop_right' ,c_size_t),
                ('private_ref', POINTER(AVBufferRef)))
#AVFrame

class AVPacket(ctypes.Structure): #avcodec.h 
    _fields_ = (('buf', POINTER(AVBufferRef)),
                ('pts', c_int64),
                ('dts', c_int64),
                ('data', POINTER(c_uint8)),
                ('size', c_int),
                ('stream_index', c_int),
                ('flags', c_int),
                ('side_data', POINTER(c_int)), #enum AVPacketSideData
                ('side_data_elems', c_int),
                ('duration', c_int64),
                ('pos', c_int64),
                ('convergence_duration', c_int64))                
#AVPacket
class AVCodec(ctypes.Structure): #avcodec.h   
    _fields_ = (('name', c_char_p),
                ('long_name', c_char_p),
                ('type', c_int), #enum AVMediaType
                ('id', c_int), #enum AVCodecID
                ('capabilities;', c_int),
                ('supported_framerates', POINTER(AVRational)),
                ('pix_fmts', POINTER(c_int)),#enum AVPixelFormat
                ('supported_samplerates', POINTER(c_int)),
                ('sample_fmts', POINTER(c_int)),#enum AVSampleFormat
                ('channel_layouts', POINTER(c_uint64)),
                ('max_lowres', c_uint8),
                ('priv_class', POINTER(AVClass)),
                ('profiles', POINTER(AVProfile)),
                ('wrapper_name', c_char_p),
                ('priv_data_size', c_int),
                ('next', POINTER(AVCodec)),
                ('init_thread_copy', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext)))),
                ('update_thread_context', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(AVCodecContext)))), #*dst, *src
                ('defaults', POINTER(AVCodecDefault)),
                ('init_static_data', POINTER(CFUNCTYPE(None,POINTER(AVCodec)))),
                ('init', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext)))),
                ('encode_sub', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(c_uint8),c_int,POINTER(AVSubtitle)))),
                ('encode2', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(AVPacket),POINTER(AVFrame),POINTER(c_int)))),
                ('decode', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),c_void_p,POINTER(c_int),POINTER(AVPacket)))),
                ('close', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext)))),
                ('send_frame', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(AVFrame)))),
                ('receive_packet', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(AVPacket)))),
                ('receive_frame', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(AVFrame)))),
                ('flush', POINTER(CFUNCTYPE(None,POINTER(AVCodecContext)))),
                ('caps_internal', c_int),
                ('bsfs', c_char_p),
                ('hw_configs', POINTER(POINTER(AVCodecHWConfigInternal)))           
    )
#AVCodec    
class AVCodecContext(ctypes.Structure): #avcodec.h   
    _fields_ = (('av_class', POINTER(AVClass)),
                ('log_level_offset', c_int),
                ('codec_type', c_int),#enum AVMediaType
                ('codec', POINTER(AVCodec)), 
                ('codec_id', c_int), #enum AVCodecID
                ('codec_tag', c_uint),
                ('priv_data', c_void_p),
                ('internal', POINTER(AVCodecInternal)),
                ('opaque', c_void_p),
                ('bit_rate', c_int64),
                ('bit_rate_tolerance', c_int),
                ('global_quality', c_int),
                ('compression_level', c_int),
                ('flags', c_int),
                ('flags2', c_int),
                ('extradata', POINTER(c_uint8)),
                ('extradata_size', c_int),
                ('time_base', AVRational),
                ('ticks_per_frame', c_int),
                ('delay', c_int),
                ('width', c_int),
                ('height', c_int),
                ('coded_width', c_int),
                ('coded_height', c_int),
                ('gop_size', c_int),
                ('pix_fmt', c_int), #enum AVPixelFormat
                ('draw_horiz_band', POINTER(CFUNCTYPE(None,POINTER(AVCodecContext),POINTER(AVFrame),c_int*AV_NUM_DATA_POINTERS,c_int,c_int,c_int))),
                ('get_format', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(c_int)))), #both c_int are enum AVPixelFormat
                ('max_b_frames', c_int),                
                ('b_quant_factor', c_float),
                ('b_frame_strategy', c_int),
                ('b_quant_offset', c_float),
                ('has_b_frames', c_int),
                ('mpeg_quant', c_int),
                ('i_quant_factor', c_float),
                ('i_quant_offset', c_float),
                ('lumi_masking', c_float),
                ('temporal_cplx_masking', c_float),
                ('spatial_cplx_masking', c_float),
                ('p_masking', c_float),
                ('dark_masking', c_float),
                ('slice_count', c_int),
                ('prediction_method', c_int),
                ('slice_offset', POINTER(c_int)),
                ('sample_aspect_ratio', AVRational),
                ('me_cmp', c_int),
                ('me_sub_cmp', c_int),
                ('mb_cmp', c_int),
                ('ildct_cmp', c_int),
                ('dia_size', c_int),
                ('last_predictor_count', c_int),
                ('pre_me', c_int),
                ('me_pre_cmp', c_int),
                ('pre_dia_size', c_int),
                ('me_subpel_quality', c_int),
                ('me_range', c_int),
                ('slice_flags', c_int),
                ('mb_decision', c_int),
                ('intra_matrix', POINTER(c_uint16)),
                ('inter_matrix', POINTER(c_uint16)),
                ('scenechange_threshold', c_int),
                ('noise_reduction', c_int),
                ('intra_dc_precision', c_int),
                ('skip_top', c_int),
                ('skip_bottom', c_int),
                ('mb_lmin', c_int),
                ('mb_lmax', c_int),
                ('me_penalty_compensation', c_int),
                ('bidir_refine', c_int),
                ('brd_scale', c_int),
                ('keyint_min', c_int),
                ('refs', c_int),
                ('chromaoffset', c_int),
                ('mv0_threshold', c_int),
                ('b_sensitivity', c_int),
                ('color_primaries', c_int),#enum AVColorPrimaries
                ('color_trc', c_int),#enum AVColorTransferCharacteristic
                ('colorspace', c_int),#enum AVColorSpace
                ('color_range', c_int),#enum AVColorRange
                ('chroma_sample_location', c_int),#enum AVChromaLocation
                ('slices', c_int),
                ('field_order', c_int),#enum AVFieldOrder
                ('sample_rate', c_int),
                ('channels', c_int),
                ('sample_fmt', c_int),#enum AVSampleFormat
                ('frame_size', c_int),
                ('frame_number', c_int),
                ('block_align', c_int),
                ('cutoff', c_int),
                ('channel_layout', c_uint64),
                ('request_channel_layout', c_uint64),
                ('audio_service_type', c_int),#enum AVAudioServiceType
                ('request_sample_fmt', c_int),#enum AVSampleFormat
                ('get_buffer2', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),POINTER(AVFrame),c_int))),
                ('refcounted_frames', c_int),
                ('qcompress', c_float),
                ('qblur', c_float),
                ('qmin', c_int),
                ('qmax', c_int),
                ('max_qdiff', c_int),
                ('rc_buffer_size', c_int),
                ('rc_override_count', c_int),
                ('rc_override', POINTER(RcOverride)),
                ('rc_max_rate', c_int64),
                ('rc_min_rate', c_int64),
                ('rc_max_available_vbv_use', c_float),
                ('rc_min_vbv_overflow_use', c_float),
                ('rc_initial_buffer_occupancy', c_int),
                ('coder_type', c_int),
                ('context_model', c_int),
                ('frame_skip_threshold', c_int),
                ('frame_skip_factor', c_int),
                ('frame_skip_exp', c_int),
                ('frame_skip_cmp', c_int),
                ('trellis', c_int),
                ('min_prediction_order' ,c_int),
                ('max_prediction_order' ,c_int),
                ('timecode_frame_start' ,c_int64),
                ('rtp_callback',POINTER(CFUNCTYPE(None,POINTER(AVCodecContext),c_void_p,c_int,c_int))),
                ('rtp_payload_size', c_int),
                ('int mv_bits'     , c_int),
                ('header_bits'     , c_int),
                ('i_tex_bits'      , c_int),
                ('p_tex_bits'      , c_int),
                ('i_count'         , c_int),
                ('p_count'         , c_int),
                ('skip_count'      , c_int),
                ('misc_bits'       , c_int),
                ('frame_bits'      , c_int),
                ('stats_out', c_char_p),
                ('stats_in', c_char_p),
                ('workaround_bugs', c_int),
                ('strict_std_compliance', c_int),
                ('error_concealment', c_int),
                ('debug', c_int),
                ('debug_mv', c_int),
                ('err_recognition', c_int),
                ('reordered_opaque', c_int64),
                ('hwaccel', POINTER(AVHWAccel)),
                ('hwaccel_context', c_void_p),
                ('error', c_uint64*AV_NUM_DATA_POINTERS),
                ('dct_algo', c_int),
                ('idct_algo', c_int),
                ('bits_per_coded_sample', c_int),
                ('bits_per_raw_sample', c_int),
                ('lowres', c_int),
                ('coded_frame', POINTER(AVFrame)),
                ('thread_count', c_int),
                ('thread_type', c_int),
                ('active_thread_type', c_int),
                ('thread_safe_callbacks', c_int),
                ('execute', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext), POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),c_void_p))   ,c_void_p,POINTER(c_int),c_int,c_int))),
                ('execute2', POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext), POINTER(CFUNCTYPE(c_int,POINTER(AVCodecContext),c_void_p,c_int,c_int))   ,c_void_p,POINTER(c_int),c_int))),
                ('nsse_weight', c_int),
                ('profile', c_int),
                ('level', c_int),
                ('skip_loop_filter', c_int),#enum AVDiscard
                ('skip_idct', c_int),#enum AVDiscard
                ('skip_frame', c_int),#enum AVDiscard
                ('subtitle_header', POINTER(c_uint8)),
                ('subtitle_header_size', c_int),
                ('vbv_delay', c_int64),
                ('side_data_only_packets', c_int),
                ('initial_padding', c_int),
                ('framerate', AVRational),
                ('sw_pix_fmt', c_int),#enum AVPixelFormat
                ('pkt_timebase', AVRational),
                ('codec_descriptor', POINTER(AVCodecDescriptor)),
                #('lowres', c_int),
                ('pts_correction_num_faulty_pts',c_int64),
                ('pts_correction_num_faulty_dts',c_int64),
                ('pts_correction_last_pts'      ,c_int64),
                ('pts_correction_last_dts'      ,c_int64),
                ('sub_charenc', c_char_p),
                ('sub_charenc_mode', c_int),
                ('skip_alpha', c_int),
                ('seek_preroll', c_int),
                #('debug_mv', c_int),
                ('chroma_intra_matrix', POINTER(c_uint16)),
                ('dump_separator', POINTER(c_uint8)),
                ('codec_whitelist', c_char_p),
                ('properties', c_uint),
                ('coded_side_data', POINTER(c_int)),#enum AVPacketSideData
                ('nb_coded_side_data', c_int),
                ('hw_frames_ctx', POINTER(AVBufferRef)),
                ('sub_text_format', c_int),
                ('trailing_padding', c_int),
                ('max_pixels', c_int64),
                ('hw_device_ctx', POINTER(AVBufferRef)),
                ('hwaccel_flags', c_int),
                ('apply_cropping', c_int),
                ('extra_hw_frames', c_int)              
    )
#AVCodecContext

class AVCodecParameters(ctypes.Structure): #avcodec.h 
    _fields_ = [
        ('codec_type', c_int), #enum AVMediaType
        ('codec_id', c_int), #enum AVCodecID
        ('codec_tag', c_uint32),
        ('extradata', POINTER(c_uint8)),
        ('extradata_size', c_int),
        ('format', c_int),
        ('bit_rate', c_int64),
        ('bits_per_coded_sample', c_int),
        ('bits_per_raw_sample', c_int),
        ('profile', c_int),
        ('level', c_int),
        ('width', c_int),
        ('height', c_int),
        ('sample_aspect_ratio', AVRational),
        ('field_order', c_int), #enum
        ('color_range', c_int), #enum
        ('color_primaries', c_int), #enum
        ('color_trc', c_int), #enum
        ('color_space', c_int), #enum
        ('chroma_location', c_int), #enum
        ('video_delay', c_int),
        ('channel_layout', c_uint64),
        ('channels', c_int),
        ('sample_rate', c_int),
        ('block_align', c_int),
        ('frame_size', c_int),
        ('initial_padding', c_int),
        ('trailing_padding', c_int),
        ('seek_preroll', c_int),
    ]
    
av_format_control_message=POINTER(CFUNCTYPE(c_int,POINTER(AVFormatContext),c_int,c_void_p,c_size_t))
MAX_REORDER_DELAY=16
class AVStream(Structure):
    _fields_ = [
        ('index', c_int),
        ('id', c_int),
        ('codec', POINTER(AVCodecContext)),
        ('priv_data', c_void_p),
        #!('pts', AVFrac),
        ('time_base', AVRational),
        ('start_time', c_int64),
        ('duration', c_int64),
        ('nb_frames', c_int64),
        ('disposition', c_int),
        ('discard', c_int), #enum AVDiscard
        ('sample_aspect_ratio', AVRational),
        ('metadata', POINTER(AVDictionary)),
        ('avg_frame_rate', AVRational),
        ('attached_pic', AVPacket),
        ('side_data', POINTER(AVPacketSideData)),
        ('nb_side_data', c_int),
        ('event_flags', c_int),
		#!
		('r_frame_rate', AVRational),
		('recommended_encoder_configuration', c_char_p),
		('codecpar', POINTER(AVCodecParameters)),
        ('info', POINTER(AVStreamInfo)),
        ('pts_wrap_bits', c_int),
        ('first_dts', c_int64),
        ('cur_dts', c_int64),
        ('last_IP_pts', c_int64),
        ('last_IP_duration', c_int),
        ('probe_packets', c_int),
        ('codec_info_nb_frames', c_int),
        ('need_parsing', c_int), #enum AVStreamParseType
        ('parser', POINTER(AVCodecParserContext)),
        ('last_in_packet_buffer', POINTER(AVPacketList)),
        ('probe_data', AVProbeData),
        ('pts_buffer', c_int64 * (MAX_REORDER_DELAY+1)),
        ('index_entries', POINTER(AVIndexEntry)),
        ('nb_index_entries', c_int),
        ('index_entries_allocated_size', c_uint),
        #!('r_frame_rate', AVRational),
        ('stream_identifier', c_int),
        ('program_num', c_int),
        ('pmt_version', c_int),
        ('pmt_stream_idx', c_int),
        ('interleaver_chunk_size', c_int64),
        ('interleaver_chunk_duration', c_int64),
        ('request_probe', c_int),
        ('skip_to_keyframe', c_int),
        ('skip_samples', c_int),
        ('start_skip_samples', c_int64),
        ('first_discard_sample', c_int64),
        ('last_discard_sample', c_int64),
        ('nb_decoded_frames', c_int),
        ('mux_ts_offset', c_int64),
        ('pts_wrap_reference', c_int64),
        ('pts_wrap_behavior', c_int),
        ('update_initial_durations_done', c_int),
        ('pts_reorder_error', c_int64 * (MAX_REORDER_DELAY+1)),
        ('pts_reorder_error_count', c_uint8 * (MAX_REORDER_DELAY+1)),
        ('last_dts_for_order_check', c_int64),
        ('dts_ordered', c_uint8),
        ('dts_misordered', c_uint8),
        ('inject_global_side_data', c_int),
        #!
        ('display_aspect_ratio', AVRational),
        #!('priv_pts', POINTER(FFFrac)),
        ('internal', POINTER(AVStreamInternal)),
        #!('codecpar', POINTER(AVCodecParameters)),
    ]
class AVFormatContext(ctypes.Structure):    
    _fields_ = (
('av_class'                       ,POINTER(AVClass)),
('iformat'                        ,POINTER(AVInputFormat)),
('oformat'                        ,POINTER(AVOutputFormat)),
('priv_data'                      ,c_void_p),
('pb'                             ,POINTER(AVIOContext)),
('ctx_flags'                      ,c_int),
('nb_streams'                     ,c_uint),
('streams'                        ,POINTER(POINTER(AVStream))),
('filename'                 ,c_byte*1024),
('url'                            ,c_char_p),
('start_time'                     ,c_int64),
('duration'                       ,c_int64),
('bit_rate'                       ,c_int64),
('packet_size'                    ,c_uint),
('max_delay'                      ,c_int),
('flags'                          ,c_int),
('probesize'                      ,c_int64),
('max_analyze_duration'           ,c_int64),
('key'                            ,POINTER(c_uint8)),
('keylen'                         ,c_int),
('nb_programs'                    ,c_uint),
('programs'                       ,POINTER(POINTER(AVProgram))),
('video_codec_id'                 ,c_int), #enum AVCodecID
('audio_codec_id'                 ,c_int), #enum AVCodecID
('subtitle_codec_id'              ,c_int), #enum AVCodecID
('max_index_size'                 ,c_uint),
('max_picture_buffer'             ,c_uint),
('nb_chapters'                    ,c_uint),
('chapters'                       ,POINTER(POINTER(AVChapter))),
('metadata'                       ,POINTER(AVDictionary)),
('start_time_realtime'            ,c_int64),
('fps_probe_size'                 ,c_int),
('error_recognition'              ,c_int),
('interrupt_callback'             ,AVIOInterruptCB),
('debug'                          ,c_int),
('max_interleave_delta'           ,c_int64),
('strict_std_compliance'          ,c_int),
('event_flags'                    ,c_int),
('max_ts_probe'                   ,c_int),
('avoid_negative_ts'              ,c_int),
('ts_id'                          ,c_int),
('audio_preload'                  ,c_int),
('max_chunk_duration'             ,c_int),
('max_chunk_size'                 ,c_int),
('use_wallclock_as_timestamps'    ,c_int),
('avio_flags'                     ,c_int),
('duration_estimation_method'     ,c_int), #enum AVDurationEstimationMethod
('skip_initial_bytes'             ,c_int64),
('correct_ts_overflow'            ,c_uint),
('seek2any'                       ,c_int),
('flush_packets'                  ,c_int),
('probe_score'                    ,c_int),
('format_probesize'               ,c_int),
('codec_whitelist'                ,c_char_p),
('format_whitelist'               ,c_char_p),
('internal'                       ,POINTER(AVFormatInternal)),
('io_repositioned'                ,c_int),
('video_codec'                    ,POINTER(AVCodec)),
('audio_codec'                    ,POINTER(AVCodec)),
('subtitle_codec'                 ,POINTER(AVCodec)),
('data_codec'                     ,POINTER(AVCodec)),
('metadata_header_padding'        ,c_int),
('opaque'                         ,c_void_p),
('control_message_cb'             ,av_format_control_message), #typedef was function pointer. but here is not
('output_ts_offset'               ,c_int64),
('dump_separator'                 ,c_uint8),
('data_codec_id'                  ,c_int), #enum AVCodecID
('open_cb'                        ,POINTER(CFUNCTYPE(c_int,POINTER(AVFormatContext),POINTER(POINTER(AVIOContext)),c_char_p,c_int,POINTER(AVIOInterruptCB),POINTER(POINTER(AVDictionary))))),
('protocol_whitelist'             ,c_char_p),
('io_open'                        ,POINTER(CFUNCTYPE(c_int,POINTER(AVFormatContext),POINTER(POINTER(AVIOContext)),c_char_p,c_int,POINTER(POINTER(AVDictionary))))),
('io_close'                       ,POINTER(CFUNCTYPE(None,POINTER(AVFormatContext),POINTER(AVIOContext)))),
('protocol_blacklist'             ,c_char_p),
('max_streams'                    ,c_int),
('skip_estimate_duration_from_pts',c_int))

   
class SwsFilter(ctypes.Structure):    
    pass

class SwsContext(ctypes.Structure):    #swscale_internal.h
    pass

'''
'''
import os

os.environ['PATH']='C:\\sw\\ffmpeg-20180702-3c4af57-win64-shared\\bin' #location of avcodec-58.dll
avcodec=WinDLL('avcodec-58.dll')
avutil=WinDLL('avutil-56.dll')
avformat=WinDLL('avformat-58.dll')
swscale=WinDLL('swscale-5.dll')
#https://gist.github.com/Neon22/eb5af7bcdcdfa2ab7d22c3d27e018bbd


avformat.avformat_open_input.argtypes=[POINTER(POINTER(AVFormatContext)),c_char_p,POINTER(AVInputFormat),POINTER(POINTER(AVDictionary))]
avformat.avformat_open_input.restype=c_int
avformat.avformat_find_stream_info.argtypes=[POINTER(AVFormatContext),POINTER(POINTER(AVDictionary))]
avformat.avformat_find_stream_info.restype=c_int
avformat.avformat_close_input.argtypes=[POINTER(POINTER(AVFormatContext))]
avformat.av_find_best_stream.argtypes=[POINTER(AVFormatContext),c_int,c_int,c_int,POINTER(POINTER(AVCodec)),c_int]
avformat.av_find_best_stream.restype=c_int
avformat.av_read_frame.argtypes=[POINTER(AVFormatContext),POINTER(AVPacket)]
avformat.av_read_frame.restype=c_int

avcodec.av_init_packet.argtypes=[POINTER(AVPacket)]
avcodec.av_init_packet.restype=None
avcodec.av_packet_unref.argtypes=[POINTER(AVPacket)]
avcodec.av_packet_unref.restype=None
#AVCodec *avcodec_find_encoder(enum AVCodecID id);
avcodec.avcodec_find_decoder.argtypes=[c_int]
avcodec.avcodec_find_decoder.restype=POINTER(AVCodec)
#AVCodec *avcodec_find_encoder(enum AVCodecID id);
avcodec.avcodec_find_encoder.argtypes=[c_int]
avcodec.avcodec_find_encoder.restype=POINTER(AVCodec)
#AVCodecContext *avcodec_alloc_context3(const AVCodec *codec);
avcodec.avcodec_alloc_context3.argtypes=[POINTER(AVCodec)]
avcodec.avcodec_alloc_context3.restype=POINTER(AVCodecContext)
avcodec.avcodec_parameters_to_context.argtypes=[POINTER(AVCodecContext),POINTER(AVCodecParameters)]
avcodec.avcodec_parameters_to_context.restype=c_int
avcodec.avcodec_open2.argtypes=[POINTER(AVCodecContext),POINTER(AVCodec),POINTER(POINTER(AVDictionary))]
avcodec.avcodec_open2.restype=c_int
avcodec.avcodec_decode_video2.argtypes=[POINTER(AVCodecContext),POINTER(AVFrame),POINTER(c_int),POINTER(AVPacket)]
avcodec.avcodec_decode_video2.restype=c_int
#int avpicture_get_size(enum AVPixelFormat pix_fmt, int width, int height);
avcodec.avcodec_free_context.argtypes=[POINTER(POINTER(AVCodecContext))]
#int avcodec_encode_video2(AVCodecContext *avctx, AVPacket *avpkt,
#          const AVFrame *frame, int *got_packet_ptr);
avcodec.avcodec_encode_video2.argtypes=[POINTER(AVCodecContext),POINTER(AVPacket),POINTER(AVFrame),POINTER(c_int)]
avcodec.avcodec_encode_video2.restype=c_int
#void avcodec_free_context(AVCodecContext **avctx);
avcodec.avcodec_free_context.argtypes=[POINTER(POINTER(AVCodecContext))]
avcodec.avcodec_free_context.restype=None    
avcodec.avpicture_get_size.argtypes=[c_int,c_int,c_int]
avcodec.avpicture_get_size.restype=c_int

avutil.av_frame_alloc.restype=POINTER(AVFrame)
avutil.av_frame_free.argtypes=[POINTER(POINTER(AVFrame))]
avutil.av_freep.argtypes=[c_void_p]
avutil.av_malloc.argtypes=[c_int]
avutil.av_malloc.restype=c_void_p#POINTER(c_ubyte)
avutil.av_adler32_update.argtypes=[c_ulong,POINTER(c_uint8),c_int]
avutil.av_adler32_update.restype=c_ulong
avutil.av_image_get_buffer_size.argtypes=[c_int,c_int,c_int,c_int]
avutil.av_image_get_buffer_size.restype=c_int
avutil.av_image_copy_to_buffer.argtypes=[POINTER(c_uint8),c_int,                
POINTER(c_uint8)*4,c_int*4,
c_int,c_int,c_int,c_int]
avutil.av_image_copy_to_buffer.restype=c_int

#struct SwsContext *sws_getContext(int srcW, int srcH, enum AVPixelFormat srcFormat,
                #int dstW, int dstH, enum AVPixelFormat dstFormat,
                #int flags, SwsFilter *srcFilter,
                #SwsFilter *dstFilter, const double *param);
swscale.sws_getContext.argtypes=[c_int,c_int,c_int,
c_int,c_int,c_int,
c_int,POINTER(SwsFilter),
POINTER(SwsFilter),POINTER(c_double)]
swscale.sws_getContext.restype=POINTER(SwsContext)
#int sws_scale(struct SwsContext *c, const uint8_t *const srcSlice[],
#const int srcStride[], int srcSliceY, int srcSliceH,
#uint8_t *const dst[], const int dstStride[]);
#swscale.sws_scale.argtypes=[POINTER(SwsContext),POINTER(c_uint8)*4,
#c_int*4,c_int,c_int,
#POINTER(c_uint8)*8,c_int*8]
swscale.sws_scale.restype=c_int

AV_PIX_FMT_RGB24=2
PIX_FMT_RGB24=AV_PIX_FMT_RGB24
SWS_BILINEAR=2
AV_PIX_FMT_YUVJ420P=12
AVMEDIA_TYPE_VIDEO = 0
AV_NOPTS_VALUE=c_int64(0x8000000000000000)    #((int64_t)UINT64_C(0x8000000000000000))

'''
run main
'''

if __name__=='__main__':
    None
