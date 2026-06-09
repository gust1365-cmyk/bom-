#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOM 소요량 계산기 - 데스크탑 앱 래퍼
PyWebView를 사용해 HTML 파일을 윈도우 앱으로 실행합니다.
"""

import sys
import os
import webview


def resource_path(relative_path):
    """PyInstaller 패키징 후에도 리소스 경로를 올바르게 반환"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)


def main():
    html_path = resource_path('BOM_소요량계산기.html')
    html_url  = 'file:///' + html_path.replace('\\', '/')

    window = webview.create_window(
        title='BOM 소요량 계산기',
        url=html_url,
        width=1280,
        height=820,
        min_size=(900, 600),
        resizable=True,
    )

    webview.start(debug=False)


if __name__ == '__main__':
    main()
