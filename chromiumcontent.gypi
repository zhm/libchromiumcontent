{
  'variables': {
    # We're not using Chromium's clang, so we can't use their plugins either.
    'clang_use_chrome_plugins': 0,
    # The Linux build of libchromiumcontent.so depends on, but doesn't
    # provide, tcmalloc by default.  Disabling tcmalloc here also prevents
    # any conflicts when linking to binaries or libraries that don't use
    # tcmalloc.
    'linux_use_tcmalloc': 0,
  },
  'target_defaults': {
    'xcode_settings': {
      'WARNING_CFLAGS!': [
        # Xcode 5 doesn't support -Wno-deprecated-register.
        '-Wno-deprecated-register',
      ],
    },
  },
}
