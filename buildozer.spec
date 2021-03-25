[app]
title = Elias OSC
package.name = EliasOSC
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,oscpy
orientation = portrait
author = Elias Kesh
android.presplash_color = 

# (list) Permissions
android.permissions = INTERNET,CHANGE_WIFI_MULTICAST_STATE,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# (int) Android API to use
# see https://developer.android.com/distribute/best-practices/develop/target-sdk
android.api = 27

# (int) Minimum API required
#android.minapi = 19

# (int) Android SDK version to use
android.sdk = 23

# (str) Android NDK version to use
#android.ndk = 19c
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = /usr/src/Android/android-ndk-r22


#android.permissions = INTERNET,READ_LOGS
#android.api = 19
#android.minapi = 19
#android.sdk = 20
#android.ndk = 21

android.private_storage = True
android.skip_update = False
fullscreen = False
android.wakelock = False
android.arch = armeabi-v7a


[buildozer]
log_level = 2
