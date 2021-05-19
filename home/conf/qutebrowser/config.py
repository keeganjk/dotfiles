config.load_autoconfig(False)

from theme_comfy3 import *

# Backend
c.backend = 'webengine'

# User agent
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Images
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

# JavaScript
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# Cookies
config.set('content.cookies.accept', 'no-3rdparty', 'chrome-devtools://*')
config.set('content.cookies.accept', 'no-3rdparty', 'devtools://*')

#config.set('content.notifications.enabled', True, 'https://www.example.com')
#config.set('content.notifications.enabled', ask, 'https://www.example.com')

# External handling
c.editor.command = ['st', '-e', 'nvim', '+call cursor({line}, {column})', '{file}']
c.fileselect.handler = 'external'
c.fileselect.folder.command = ['st', '-f', '"AW Greybeard-10"', '-e', 'ranger', '--choosedir={}']

# Tabs / pages
c.tabs.show = 'multiple'
c.tabs.position = 'left'
c.tabs.width = 90
c.url.default_page = 'about:blank'
c.url.start_pages = 'about:blank'

# Search engines
homepage = 'https://searx.fmac.xyz'
searx_customized = homepage + '/?preferences=eJxtVcGO2zgM_Zr1xUiB2R725MNiF0ULLDBFJ92rQUuMzVoSXUpOxvv1Szl2okznECOiycdH8ok2kLBnIYxNjwEFXOUg9DP02GA4fH-pHBtw-VDBnNiwnxwmbCry6tNOwq9Lc5QZK49pYNt8fX45VhFOGBHEDM1TlQb02HA0IJVgnF2KLYc24KVN0DWfwEWsLFOrL9mdURoGPX5g6as16hDTohQc92TY4vlgQcYK7BmCQdtuiTYcitA5tWLoKeSyqFcDxNS2W4W__f5Xjzgm8hjblpKeKZzJEs969nMkoyY7WwxlTEQPIZGpoxnYgbRtNITKQN89vSpQbkhcHf8L4MvQzI_OWFMsrZ5_KI0HWpQcdBunMPntX-Jx4cRx4BHCnaHMXittW6WOnBNfaKSOeXzIMpIZIRaF9cy9w3pysNSez5Sb8AChg1FTfqoBE7N7AFz6PrEIhlTEBdC5lV4dpW42I6athgx85iVrpsSCgbk0qFsiDiBLaQ0LwL2Ap48f_3gtcsM01p5EWAmcyK0zKEnuNkFrKd0qWxmhREoPuXav9wveOaDwhWzpZYw5pHNBK0u1Q-m3BpwEsY58ShcQrC0JGkVdtrfXofxa801UJwEPjjrBLULmbunRx_c1cmNxG_99VCvw7Xi9PZlsnR-7-FanvXM5r46kzuzio4gddzHhB9l5zCGqsuJQUN87GtkQuNqjJViVtXgOTuVW4hU38UZxAE2fH1sOv3j02rs6CYTodIXZ9yZ4I_CmN3tVumzIbpONd_OEKGnuyovFEwbBiQsva_va4okCZb3GNxqmnzOnh7qsXob867m-8ioXRgJJ05urQaGcUnlpYZoKIjlb5FnMQ_RJKIwEplSQFc6S3QPNnCs3y1vqFhK8u0DWwArD4369b9zJzWqKzbN2q_3TGNSgv5-_6Fq_CKW8Jr-EtWGom1PYZfB_yR8cjdgOnEZc7vA72FFAt4i037_9o0C6r1A07AXdqVU0Fg9r_9X2OavuGrZ6ZFnn74y5fuIW_U44vXPZ83j8-rLTqlQdqIn-Bw2cqHI=&q={}'
c.url.searchengines = {'DEFAULT': searx_customized, 'az': 'https://www.amazon.com/s?k={}', 'ub': 'https://www.urbandictionary.com/define.php?term={}', 'at': 'https://alternativeto.net/browse/search?q={}', '4g': 'https://boards.4channel.org/g/catalog#s={}', '4mu': 'https://boards.4channel.org/mu/catalog#s={}', 'yx': 'https://yandex.com/search/?text={}', 'yxi': 'https://yandex.com/images/search?text={}', 'dcc': 'https://www.dict.cc/?s={}' }

# Colors / theming
config.set("colors.webpage.darkmode.enabled", True)
c.colors.webpage.darkmode.algorithm = 'lightness-hsl'
c.hints.border = c15
c.colors.completion.fg = c07
c.colors.completion.odd.bg = cbg
c.colors.completion.even.bg = cbg
c.colors.completion.category.fg = c04
c.colors.completion.category.bg = c00 #'#151515'
c.colors.completion.category.border.top = cbg
c.colors.completion.category.border.bottom = cbg
c.colors.completion.item.selected.fg = cbg
c.colors.completion.item.selected.bg = c04
c.colors.completion.item.selected.border.top = c06
c.colors.completion.item.selected.border.bottom = c06
c.colors.completion.item.selected.match.fg = c11
c.colors.completion.match.fg = c04
c.colors.completion.scrollbar.fg = c07
c.colors.completion.scrollbar.bg = c00
c.colors.contextmenu.menu.bg = cbg
c.colors.contextmenu.menu.fg = c07
c.colors.contextmenu.selected.bg = c04
c.colors.contextmenu.selected.fg = c07
c.colors.contextmenu.disabled.bg = cbg
c.colors.contextmenu.disabled.fg = c01
c.colors.downloads.bar.bg = cbg
c.colors.downloads.start.fg = c07
c.colors.downloads.start.bg = c00
c.colors.downloads.stop.fg = c15
c.colors.downloads.stop.bg = c02
c.colors.downloads.error.fg = c15
c.colors.downloads.error.bg = c09
c.colors.hints.fg = c15
c.colors.hints.bg = c04
c.colors.hints.match.fg = c02
c.colors.messages.error.fg = c15
c.colors.messages.error.bg = c09
c.colors.messages.error.border = c00
c.colors.messages.warning.fg = cbg
c.colors.messages.warning.bg = c03
c.colors.messages.warning.border = c00
c.colors.messages.info.fg = c07
c.colors.messages.info.bg = cbg
c.colors.messages.info.border = c00
c.colors.prompts.fg = c07
c.colors.prompts.border = c00
c.colors.prompts.bg = cbg
c.colors.prompts.selected.bg = c02
c.colors.statusbar.normal.fg = c07
c.colors.statusbar.normal.bg = cbg
c.colors.statusbar.insert.fg = c15
c.colors.statusbar.insert.bg = c02
c.colors.statusbar.passthrough.fg = c15
c.colors.statusbar.passthrough.bg = c06
c.colors.statusbar.private.fg = c07
c.colors.statusbar.private.bg = cbg
c.colors.statusbar.command.fg = c07
c.colors.statusbar.command.bg = cbg
c.colors.statusbar.command.private.fg = cbg
c.colors.statusbar.command.private.bg = c07
c.colors.statusbar.caret.fg = c07
c.colors.statusbar.caret.bg = c05
c.colors.statusbar.caret.selection.fg = c07
c.colors.statusbar.caret.selection.bg = c05
c.colors.statusbar.progress.bg = c07
c.colors.statusbar.url.fg = c15
c.colors.statusbar.url.error.fg = c09
c.colors.statusbar.url.hover.fg = c06
c.colors.statusbar.url.success.http.fg = c07
c.colors.statusbar.url.success.https.fg = c02
c.colors.statusbar.url.warn.fg = c06
c.colors.tabs.bar.bg = cbg
c.colors.tabs.indicator.start = c04
c.colors.tabs.indicator.stop = c04
c.colors.tabs.indicator.error = cbg
c.colors.tabs.odd.fg = c07
c.colors.tabs.odd.bg = cbg
c.colors.tabs.even.fg = c07
c.colors.tabs.even.bg = cbg
c.colors.tabs.selected.odd.fg = c15
c.colors.tabs.selected.odd.bg = c08
c.colors.tabs.selected.even.fg = c15
c.colors.tabs.selected.even.bg = c08
c.colors.tabs.pinned.odd.fg = c07
c.colors.tabs.pinned.odd.bg = c04
c.colors.tabs.pinned.even.fg = c07
c.colors.tabs.pinned.even.bg = c04
c.colors.tabs.pinned.selected.odd.fg = c07
c.colors.tabs.pinned.selected.odd.bg = c04
c.colors.tabs.pinned.selected.even.fg = c07
c.colors.tabs.pinned.selected.even.bg = c04
c.colors.webpage.bg = cbg

# Fonts
c.fonts.default_family = 'Latin Modern Math'
c.fonts.default_size = '16px'
c.fonts.completion.entry = '16px "AW Greybeard"'
c.fonts.completion.category = 'bold 16px "AW Greybeard"'
c.fonts.contextmenu = '16px "AW Greybeard"'
c.fonts.debug_console = '16px "AW Greybeard"'
c.fonts.downloads = '16px "AW Greybeard"'
c.fonts.hints = 'bold 16px "AW Greybeard"'
c.fonts.keyhint = '16px "AW Greybeard"'
c.fonts.messages.error = '16px "AW Greybeard"'
c.fonts.messages.info = '16px "AW Greybeard"'
c.fonts.messages.warning = '16px "AW Greybeard"'
c.fonts.prompts = '16px "AW Greybeard"'
c.fonts.statusbar = '16px "AW Greybeard"'
c.fonts.tabs.selected = '16px "AW Greybeard"'
c.fonts.tabs.unselected = '16px "AW Greybeard"'
c.fonts.web.family.standard = 'Latin Modern Math'
c.fonts.web.family.fixed = 'Fira Code'
c.fonts.web.family.serif = 'Latin Modern Math'
c.fonts.web.family.sans_serif = 'Noto Sans'
c.fonts.web.size.default_fixed = 13

# Bindings / aliases
c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}
c.bindings.key_mappings = {'<Ctrl+6>': '<Ctrl+^>', '<Ctrl+Enter>': '<Ctrl+Return>', '<Ctrl+i>': '<Tab>', '<Ctrl+j>': '<Return>', '<Ctrl+m>': '<Return>', '<Ctrl+[>': '<Escape>', '<Enter>': '<Return>', '<Shift+Enter>': '<Return>', '<Shift+Return>': '<Return>'}
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('Z', 'hint links spawn st -e youtube-dl {hint-url}')
config.bind('t', 'set-cmd-text -s :open -t')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind('W', ':open -w ' + homepage)
config.bind('I', ':open -p ' + homepage)
config.bind('z', ':config-cycle tabs.position left top')

# CSS Stylesheets
#c.content.user_stylesheets = ['~/conf/qutebrowser/css/my.css']
config.bind('<Ctrl-R>', 'config-cycle content.user_stylesheets "~/.config/qutebrowser/css/my.css" ""')
