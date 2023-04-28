import subprocess
import re


def define_udid_device():
    process = subprocess.Popen(
        ['adb', 'devices'],
        stdout=subprocess.PIPE
    )
    result_stdout = str(process.communicate()[0], 'UTF-8')
    udid_device = re.sub(r'Listofdevicesattached|device', '', re.sub(r'\s|[\n]', '', result_stdout))
    return udid_device


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '11',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': define_udid_device(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
    }
