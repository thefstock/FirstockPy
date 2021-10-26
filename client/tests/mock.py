"""
Includes mock results for every endpoint and a function to mock post method
"""
import json
from py_client.modules.watchlists import endpoints as wlep
from py_client.modules.users import endpoints as uep
from py_client.modules.alerts import endpoints as aep

# MOCK RESULTS
RESULTS = {
    # Alerts module
    aep.SET_ALERT: {
        "request_time": "11:22:26 08-04-2021",
        "stat": "Oi created",
        "al_id": "21040800000004"
    },
    aep.CANCEL_ALERT: {
        "request_time": "15:03:33 08-04-2021",
        "stat": "Oi delete success",
        "al_id": "21040800000008"
    },
    aep.MODIFY_ALERT: {
        "request_time": "16:36:42 08-04-2021",
        "stat": "Oi Replaced",
        "al_id": "21040800000013"
    },
    aep.GET_PENDING_ALERT: {
        "stat": "Ok",
        "ai_t": "LTP_A",
        "al_id": "21040800000008",
        "tsym": "ACC-EQ",
        "exch": "NSE",
        "token": "22",
        "remarks": "test",
        "validity": "DAY",
        "d": "95000.00"
    },
    aep.GET_ENABLED_ALERT_TYPES: {
        "stat": "Ok",
        "request_time": "10:02:06 15-04-2021",
        "ai_ts": [
            {"ai_t": "ATP"},
            {"ai_t": "LTP"},
            {"ai_t": "Perc. Change"}
        ]
    },
    aep.PLACE_GTT_ORDER: {
        "request_time": "10:02:06 15-04-2021",
        "stat": "Oi created",
        "al_id": "21041500000010"
    },
    aep.MODIFY_GTT_ORDER: {
        "request_time": "12:15:18 15-04-2021",
        "stat": "Oi Replaced",
        "al_id": "21041500000008"
    },
    aep.CANCEL_GTT_ORDER: {
        "request_time": "12:20:01 15-04-2021",
        "stat": "Oi delete success",
        "al_id": "21041500000013"
    },
    aep.GET_PENDING_GTT_ORDER: {
        "stat": "Ok",
        "ai_t": "LTP_A",
        "al_id": "21041500000002",
        "tsym": "ACC-EQ",
        "exch": "NSE",
        "token": "22",
        "remarks": "test",
        "validity": "DAY",
        "actid": "MOHINI",
        "trantype": "B",
        "prctyp": "LMT",
        "qty": 1,
        "prc": "1305.00",
        "prd": "C",
        "ordersource": "MOB",
        "d": "1900.00"
    },
    aep.GET_ENABLED_GTTS: {
        "stat": "Ok",
        "request_time": "12:20:01 15-04-2021",
        "ai_ts": [
            {"ai_t": "ATP"},
            {"ai_t": "LTP"}
        ]
    },
    aep.GET_UNSETTLED_TRADING_DATE: {
        "stat": "Ok",
        "request_time": "12:20:01 15-04-2021",
        "trd_date": [
            {
                "trd_date": "28-04-2021"
            },
            {
                "trd_date": "29-04-2021"
            },
            {
                "trd_date": "30-04-2021"
            }
        ]
    },
    # Users Module
    uep.LOGIN: {
        "request_time": "20:18:47 19-05-2020",
        "stat": "Ok",
        "susertoken": "3b97f4c67762259a9ded6dbd7bfafe2787e662b3870422ddd343a59895f423a0",
        "lastaccesstime": "1589899727"
    },
    uep.LOGOUT: {
        "stat": "Ok",
        "request_time": "10:43:41 28-05-2020"
    },
    uep.FORGOT_PASSWORD: {
        "request_time": "10:52:56 28-05-2020",
        "stat": "Ok"
    },
    uep.CHANGE_PASSWORD: {
        "request_time": "10:20:04 27-05-2020",
        "stat": "Ok",
        "dmsg": "Password Change Success. Your new password will expire in 15"
    },
    uep.VERIFY_HS_TOKEN: 'TRUE',
    uep.SET_DEVICE_PIN: {
        "request_time": "14:59:43 27-05-2020",
        "stat": "Ok"
    },
    uep.LOGIN_WITH_DPIN: {
        "request_time": "17:01:45 27-05-2020",
        "stat": "Ok",
        "susertoken": "b0856b3f6c4bac657417fc95de3e2060567b8bd80665e0a8ab82bbde5c434936",
        "lastaccesstime": "1590579105"
    },
    uep.USER_DETAILS: {
        "request_time": "20:20:04 19-05-2020",
        "prarr": [
            {
                "prd": "C",
                "s_prdt_ali": "Delivery",
                "exch": ["NSE", "BSE"]
            },
            {
                "prd": "I",
                "s_prdt_ali": "Intraday",
                "exch": ["NSE", "BSE", "NFO"]
            },
            {
                "prd": "H",
                "s_prdt_ali": "High Leverage",
                "exch": ["NSE", "BSE", "NFO"]
            },
            {
                "prd": "B",
                "s_prdt_ali": "Bracket Order",
                "exch": ["NSE", "BSE", "NFO"]
            }
        ],
        "exarr": [
            "NSE",
            "NFO"
        ],
        "orarr": [
            "MKT",
            "LMT",
            "SL-LMT",
            "SL-MKT",
            "DS",
            "2L",
            "3L",
            "4L"
        ],
        "brkname": "VIDYA",
        "brnchid": "VIDDU",
        "email": "gururaj@gmail.com",
        "actid": "GURURAJ",
        "uprev": "INVESTOR",
        "stat": "Ok"
    },
    uep.SAVE_FCM_TOKEN: {
        "request_time": "14:59:43 27-05-2020",
        "stat": "Ok"
    },
    # WatchLists
    wlep.GET_NAMES: {
        "request_time": "12:34:52 21-05-2020",
        "values": [
            "default",
            "WL"
        ],
        "stat": "Ok"
    },
    wlep.GET_WATCHLIST: {
        "request_time": "13:25:17 21-05-2020",
        "values": [
            {
                "exch": "BSE",
                "token": "972889",
                "tsym": "915PTCIF27"
            },
            {
                "exch": "NSE",
                "token": "13",
                "tsym": "ABB-EQ"
            },
            {
                "exch": "NSE",
                "token": "22",
                "tsym": "ACC-EQ"
            }
        ],
        "stat": "Ok"
    },
    wlep.SEARCH_SCRIPS: {
        "stat": "Ok",
        "values": [
            {
                "exch": "NSE",
                "token": "18069",
                "tsym": "REL100NAV-EQ"
            },
            {
                "exch": "NSE",
                "token": "24225",
                "tsym": "RELAXO-EQ"
            },
            {
                "exch": "NSE",
                "token": "4327",
                "tsym": "RELAXOFOOT-EQ"
            },
            {
                "exch": "NSE",
                "token": "18068",
                "tsym": "RELBANKNAV-EQ"
            },
            {
                "exch": "NSE",
                "token": "2882",
                "tsym": "RELCAPITAL-EQ"
            },
            {
                "exch": "NSE",
                "token": "18070",
                "tsym": "RELCONSNAV-EQ"
            },
            {
                "exch": "NSE",
                "token": "18071",
                "tsym": "RELDIVNAV-EQ"
            }
        ]
    },
    wlep.ADD_SCRIPS: {
        "request_time": "13:50:40 21-05-2020",
        "stat": "Ok"
    },
    wlep.DELETE_SCRIPS: {
        "request_time": "13:50:40 21-05-2020",
        "stat": "Ok"
    },
    wlep.GET_SECURITY_INFO: {
        "request_time": "17:43:38 31-10-2020",
        "stat": "Ok",
        "exch": "NSE",
        "tsym": "ACC-EQ",
        "cname": "ACC LIMITED",
        "symname": "ACC",
        "seg": "EQT",
        "instname": "EQ",
        "isin": "INE012A01025",
        "pp": "2",
        "ls": "1",
        "ti": "0.05",
        "mult": "1",
        "prcftr_d": "(1 / 1 ) * (1 / 1)",
        "trdunt": "ACC.BO",
        "delunt": "ACC",
        "token": "22",
        "varmrg": "40.00"
    },
    wlep.GET_QUOTES: {
        "request_time": "12:05:21 18-05-2021",
        "stat": "Ok", "exch": "NSE",
        "tsym": "ACC-EQ",
        "cname": "ACC LIMITED",
        "symname": "ACC",
        "seg": "EQT",
        "instname": "EQ",
        "isin": "INE012A01025",
        "pp": "2",
        "ls": "1",
        "ti": "0.05",
        "mult": "1",
        "uc": "2093.95",
        "lc": "1713.25",
        "prcftr_d": "(1 / 1 ) * (1 / 1)",
        "token": "22",
        "lp": "0.00",
        "h": "0.00",
        "l": "0.00",
        "v": "0",
        "ltq": "0",
        "ltt": "05:30:00",
        "bp1": "2000.00",
        "sp1": "0.00",
        "bp2": "0.00",
        "sp2": "0.00",
        "bp3": "0.00",
        "sp3": "0.00",
        "bp4": "0.00",
        "sp4": "0.00",
        "bp5": "0.00",
        "sp5": "0.00",
        "bq1": "2",
        "sq1": "0",
        "bq2": "0",
        "sq2": "0",
        "bq3": "0",
        "sq3": "0",
        "bq4": "0",
        "sq4": "0",
        "bq5": "0",
        "sq5": "0",
        "bo1": "2",
        "so1": "0",
        "bo2": "0",
        "so2": "0",
        "bo3": "0",
        "so3": "0",
        "bo4": "0",
        "so4": "0",
        "bo5": "0",
        "So5": "0"
    },
    wlep.GET_PREDEFINED_WATCHLISTS: {
        "values": [
            "NIFTY2",
            "NIFTY50"
        ]
    },
    wlep.GET_PREDEFINED_SCRIPS: {
        "stat": "Ok",
        "values": [
            {
                "exch": "NSE",
                "token": "15083",
                "tsym": "ADANIPORTS-EQ",
                "pp": "2",
                "ls": "1",
                "ti": "0.05"
            },
            {
                "exch": "NSE",
                "token": "236",
                "tsym": "ASIANPAINT-EQ",
                "pp": "2",
                "ls": "1",
                "ti": "0.05"
            },
            {
                "exch": "NSE",
                "token": "5900",
                "tsym": "AXISBANK-EQ",
                "pp": "2",
                "ls": "1",
                "ti": "0.05"
            },
            {
                "exch": "NSE",
                "token": "16669",
                "tsym": "BAJAJ-AUTO-EQ",
                "pp": "2",
                "ls": "1",
                "ti": "0.05"
            },
            {
                "exch": "NSE",
                "token": "16675",
                "tsym": "BAJAJFINSV-EQ",
                "pp": "2",
                "ls": "1",
                "ti": "0.05"
            },
            {
                "exch": "NSE",
                "token": "317",
                "tsym": "BAJFINANCE-EQ",
                "pp": "2",
                "ls": "1",
                "ti": "0.05"
            }
        ]
    },

}


def mock_post(endpoint, *args):
  """
  Mock the post method.
  Takes the response from results for corresponding endpoint and returns
  """
  result = RESULTS.get(endpoint)
  if result is not None:
    return json.dumps(result)
  else:
    raise KeyError('No sample result found for the endpoint')
