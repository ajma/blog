Resolving "SDK does not have any Build Tools installed" error
#############################################################
:date: 2013-05-18
:tags: android,android-sdk
:category: Android

After upgrading my Android SDK to 22, I started running into failed builds with the error message::

{android-sdk}/tools/ant/build.xml:479: SDK does not have any Build Tools installed

Couldn’t find very much on the web on how to resolve this and eventually I realized that it was because I only updated existing packages. In SDK 22, the platform tools and build tools are split up into their own items in the SDK manager.

Make sure you install the build-tools and platform-tools.
