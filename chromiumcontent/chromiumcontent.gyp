{
  'targets': [
    {
      'target_name': 'chromiumcontent_all',
      'type': 'none',
      'dependencies': [
        'chromiumcontent',
        'test_support_chromiumcontent',
      ],
      'conditions': [
        ['OS=="linux"', {
          'dependencies': [
            '<(DEPTH)/sandbox/sandbox.gyp:chrome_sandbox',
            '<(DEPTH)/components/components.gyp:encryptor',
          ],
          'actions': [
            {
              'action_name': 'Flatten libencryptor.a',
              'inputs': [
                '<(PRODUCT_DIR)/obj/components/libencryptor.a',
              ],
              'outputs': [
                '<(PRODUCT_DIR)/libencryptor.a',
              ],
              'action': [
                '<(DEPTH)/../../../tools/linux/ar-combine.sh',
                '-o',
                '<@(_outputs)',
                '<@(_inputs)',
              ],
            },
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            'chromiumviews',
            '<(DEPTH)/components/components.gyp:encryptor',
            '<(DEPTH)/sandbox/sandbox.gyp:sandbox_static',
          ],
        }],
      ],
    },
    {
      'target_name': 'chromiumcontent',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/base/base.gyp:base_prefs',
        '<(DEPTH)/content/content.gyp:content',
        '<(DEPTH)/content/content.gyp:content_app_both',
        '<(DEPTH)/content/content_shell_and_tests.gyp:content_shell_pak',
        '<(DEPTH)/net/net.gyp:net_with_v8',
      ],
    },
    {
      'target_name': 'test_support_chromiumcontent',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base_prefs_test_support',
        '<(DEPTH)/content/content_shell_and_tests.gyp:test_support_content',
      ],
    },
  ],
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'chromiumviews',
          'type': 'none',
          'dependencies': [
            '<(DEPTH)/ui/views/controls/webview/webview.gyp:webview',
            '<(DEPTH)/ui/views/views.gyp:views',
          ],
          'actions': [
            {
              'action_name': 'Create chromiumviews.lib',
              'inputs': [
                '<(PRODUCT_DIR)\\obj\\third_party\\iaccessible2\\iaccessible2.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\compositor\\compositor.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\views\\views.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\views\\controls\\webview\\webview.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\web_dialogs\\web_dialogs.lib',
              ],
              'outputs': [
                '<(PRODUCT_DIR)\\chromiumviews.lib',
              ],
              'action': [
                'lib.exe',
                '/nologo',
                # We can't use <(_outputs) here because that escapes the
                # backslash in the path, which confuses lib.exe.
                '/OUT:<(PRODUCT_DIR)\\chromiumviews.lib',
                '<@(_inputs)',
              ],
              'msvs_cygwin_shell': 0,
            },
          ],
        },
      ],
    }],
  ],
}
