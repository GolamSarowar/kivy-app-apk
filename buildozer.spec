[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for .apk)
package.domain = org.example

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas

# (str) The main entry point of the application
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Orientation (one of landscape, portrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (str) Full name of the main file in the source directory
source.main_file = main.py

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 1

# Android specific
# (int) Minimum API required for the application to run, e.g. 21 (Android 5.0)
android.minapi = 21

# (str) Android SDK version to use (default is set)
android.sdk = 30

# (str) Android NDK version to use (default is set)
android.ndk = 23b

# (str) Android API level to target
android.api = 30

# (str) Android SDK Build Tools version to use
android.build_tools_version = 30.0.3
