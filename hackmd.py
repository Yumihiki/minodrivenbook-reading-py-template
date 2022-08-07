"""ミノ駆動本読書py"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path


@dataclass
class MinoDrivenBookReadingPy:
    count: int
    connpass_url: str
    reading_range: str
    event_year: int
    event_month: int
    event_day: int
    event_hour: int
    event_minute: int
    chapter: list

    BOOK_READING_TIME = 30
    MAIN_TIME = 90

    def make_message(self):
        title = self._title()
        tag = self._tag()
        please = self._please()
        what_is_this_memo = self._what_is_this_memo()
        start_reading_book_time, base_time, finish_main_time = \
            self._calc_datetime()
        flow = self._flow(start_reading_book_time, base_time, finish_main_time)
        chapter = self._make_chapter()
        return title + tag + please + what_is_this_memo + flow + chapter

    def _title(self):
        return f"""# (template) ミノ駆動本_読書py[{self.count}] みんなのメモ
"""

    def _tag(self):
        return f"""
###### tags: `ミノ駆動本`

- このメモはWebに公開されています（HackMDチーム）
- リンクを知っている人は見られます
- HackMDにログインして編集できます{self.count}

"""

    def _please(self):
        return """
## お願い事項

https://twitter.com/MinoDriven/status/1541334416622256130

> 【お願い】
拙著『良いコード／悪いコードで学ぶ設計入門』に関する情報発信について。
ブログ等で発信の際は、引用の範囲を超え、著作権侵害となる場合は勿論のこと、
拙著の詳細内容が分かるような表現での公開はお控え頂けると助かります。
ご感想や拙著に基づく試行錯誤は歓迎です。 #ミノ駆動本

とミノ駆動さんが仰られていますので、勉強会そのものでも詳細内容がわかる記述はしないように気をつけていきましょう。

"""

    def _what_is_this_memo(self):
        return f"""
## このメモについて

このメモは ミノ駆動本_読書py[{self.count}] のメモです
{self.connpass_url}

読む範囲: {self.reading_range}

ミノ駆動本のサポートページより、Javaのサンプルコードが見られます。
https://gihyo.jp/book/2022/978-4-297-12783-1/support
"""

    def _flow(self, start_reading_book_time, base_time, finish_main_time):
        return f"""
## 読書会の流れ

* {start_reading_book_time}〜{base_time} **自由参加**のもくもく会（個人作業）
- 事前に読む時間がとれなかった方はここで読んじゃいましょう（ざっとで大丈夫です）
- 合わせて、この**HackMD**に話したいことを各自書いてください
        - ログインすれば書ける設定にしています
        - ここがわからん、ここはわかった　お気軽に書き込んでみてください
        - HackMDの書き込みに投票し、みんなが気になるところをわいわい読み解いていきます
* {base_time}〜{finish_main_time} 読書会本編（みんなでわいわい）
    * Discordでスライド共有して別途案内します
    * {base_time}開始の本編では、「わたしこれ気になる！」
という話題に `:+1:` と書いて投票します。
        * :+1: する上限はありません。
気になる話題に全部 :+1: しちゃいましょう。
ただし1つの話題には1個だけ:+1:でお願いします
    * 票数が多い話題から話していきます。
"""

    def _mokumoku_workzone(self):
        return """
## 以下、もくもく会ワークゾーン

### 感想、気付き

- 
- 
- 

"""

    def _kininaru(self, *args):
        return f"""
以下は各節で「これってどういうことなんだろう」
「ここからこういう気付きがあった」などを書き出すゾーンです。
{self.reading_range}章

"""

    def _make_chapter(self):
        chapter = ''
        count = 0
        for i in self.chapter:
            if count == 0:
                t = f"""
### {i}
"""
                chapter += t
                count += 1
                continue
            t = f"""
#### {i}

- 
- 
- 

"""
            chapter += t
        return chapter

    def _calc_datetime(self):
        base_time = datetime(
            self.event_year,
            self.event_month,
            self.event_day,
            self.event_hour,
            self.event_minute
        )
        start_book_reading_time = base_time - timedelta(
            minutes=self.BOOK_READING_TIME)

        finish_main_time = base_time + timedelta(minutes=self.MAIN_TIME)
        return \
            start_book_reading_time.strftime("%H:%M"), \
            base_time.strftime("%H:%M"), \
            finish_main_time.strftime("%H:%M")


if __name__ == '__main__':
    try:
        # チャプターは以下のシートを流用するとサクッと作れるようにしています
        # https://docs.google.com/spreadsheets/d/1dleM32o2iy5_QgGx9U7Ku9NGiGky7ZX0EinWDXNfi8g/edit#gid=0
        mino_driven = MinoDrivenBookReadingPy(
            count=6,
            connpass_url="https://pythonista-books.connpass.com/event/256267/",
            reading_range="10章",
            event_year=2022,
            event_month=8,
            event_day=13,
            event_hour=20,
            event_minute=00,
            chapter=[
                '10 名前設計 ―あるべき構造を見破る名前―',
                '10.1 悪魔を呼び寄せる名前',
                '10.2 名前を設計する―目的駆動名前設計',
                '10.3 設計時の注意すべきリスク',
                '10.4 意図がわからない名前',
                'Column 技術駆動命名を用いる分野もある',
                '10.5 構造を大きく歪ませてしまう名前',
                'Column クソコード動画「Managerクラス」',
                '10.6 名前的に居場所が不自然なメソッド',
                '10.7 名前の省略',
            ]
        )
    except Exception as e:
        print(f"インスタンス生成に失敗しました。異常値が無いか確認してください。")
        raise e
    try:
        p = Path("hackmd.md")
        p.touch()
        p.write_text(mino_driven.make_message())
        # with p.open(mode="w") as f:
        #     f.write(mino_driven.make_message())
        print("作成完了！ 出力されたファイルを確認してください。")
    except Exception as e:
        print(f"作成に失敗しました。")
        raise e
