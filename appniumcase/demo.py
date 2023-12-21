#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-19 18:29
# @Author : yooli
# @file : demo.py

from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='12'
desired_caps['deviceName']='emulator-16384'
# com.android.settings/com.android.settings.Settings
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print("启动【设置】应用")
driver.quit()