import requests

# step_1:指定url
url = "http://www.sogo.com"
# step_2 : 发 起 请 求 :
# 使 用 get 方 法 发 起 get 请 求 ， 该 方 法 会 返 回 一 个 响 应 对 象 。 参 数 url 表 示 请 求 对 应 的 url
response = requests.get(url=url)
# step_3 : 获 取 响 应 数 据 :
# 通 过 调 用 响 应 对 象 的 text 属 性 ， 返 回 响 应 对 象 中 存 储 的 字 符 串 形 式 的 响 应 数 据 （ 页 面 源 码 数 据 ）
page_text = response.text
# step_4:持久化储存
with open('sogo.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print("爬虫结束")
