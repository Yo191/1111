# -*- coding: utf-8 -*-
from .config import Config
import json, requests, urllib

class Server(Config):
    LINE_HOST_DOMAIN            = 'https://gw.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-tw.line-apps.com'
    LINE_TIMELINE_API           = 'https://gw.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gw.line.naver.jp/mh'

    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814'
    }

    APP_TYPE    = "CHROMEOS\t2.1.0\tCHROMEOS\t10.0.0"
    APP_VER     = "8.9.1"
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'TORRARACH TEAM HACKBOT'
    SYSTEM_VER  = '10.12.0'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = (r"[^@]+@[^@]+\.[^@]+")
    _session        = requests.session()
    timelineHeaders = {}
    Headers         = {}

    def __init__(self):
        self.Headers = {}
        self.channelHeaders = {}
        Config.__init__(self)

    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        return url + path + '?' + urllib.parse.urlencode(params)

    def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setTimelineHeadersWithDict(self, headersDict):
        self.timelineHeaders.update(headersDict)

    def setTimelineHeaders(self, argument, value):
        self.timelineHeaders[argument] = value

    def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

    def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.delete(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.put(url, headers=headers, data=data)