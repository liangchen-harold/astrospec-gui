"""
@author: Harold Liang (https://lcsky.org)
"""

import time
import asyncio
import tkinter as tk
import tkinter.filedialog
from async_tkinter_loop import async_handler, async_mainloop

# 耗时操作异步化（threading -> async/await）
from concurrent.futures.thread import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=1)
# 函数代理，因为run_in_executor只支持*args形式，转换成更加通用的**kwargs参数
def proxy(*args):
    func, kwargs = args
    func(**kwargs)
# 耗时操作通过线程池异步化，与async/await机制兼容
async def async_run(func, **kwargs):
    ts = time.time()
    try:
        ret = await asyncio.get_running_loop().run_in_executor(executor, proxy, func, kwargs)
    except Exception as error:
        raise error
    finally:
        print(f"[async_run] {time.time() - ts:.3f}s")
    return ret


# 多语言支持
import locale
lang = 'en'
default_lang = 'en'
loc = locale.getdefaultlocale()
lang = loc[0].split('_')[0]
print(loc, lang)

def _(**strs):
    if lang in strs:
        return strs[lang]
    return strs[default_lang]


# GUI逻辑
import os
import sys
import argparse
from tqdm import tqdm
from glob import glob
from pathlib import Path
import astrospec as ass
import importlib.metadata

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title(f"astrospec {importlib.metadata.version('astrospec')}")
        self.geometry("320x126")

        iconfile = "astrospec-256.ico"
        if not hasattr(sys, "frozen"):
            iconfile = os.path.join(os.path.dirname(__file__), iconfile)
        else:
            iconfile = os.path.join(sys.prefix, iconfile)
        self.iconbitmap(default=iconfile)

        # creating a frame and assigning it to container
        container = tk.Frame(self)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = MainPage(container, self)
        self.frame.grid(row=0, column=0, sticky="nsew")

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.v_folder = tk.StringVar()
        self.v_info = tk.StringVar()

        self.grid(padx=5, pady=10)
        self.columnconfigure(tuple(range(1)), weight=1)
        # self.rowconfigure(tuple(range(2)), weight=1)

        w_label = tk.Label(self, textvariable = self.v_info)
        w_label.grid(row=1, columnspan=2, padx=10, pady=10, sticky='nsew')

        w_folder = tk.Entry(self, textvariable = self.v_folder)
        w_folder.grid(row=0, column=0, padx=5, sticky='nsew')

        w_btn_folder = tk.Button(self, text = _(zh='选择文件夹', en='browse'), command=self.open_folder_selector)
        w_btn_folder.grid(row=0, column=1, padx=5, sticky='e')

        self.w_btn_run = tk.Button(
            self,
            text=_(zh='处理', en='run'),
            command=self.on_run,
        )
        self.w_btn_run.grid(row=2, column=0, padx=5, sticky='nsew')
        # self.w_btn_run.grid(row=2, columnspan=2, sticky='nsew')

        w_btn_about = tk.Button(
            self,
            text=_(zh='关于', en='about'),
            command=self.on_about,
        )
        w_btn_about.grid(row=2, column=1, padx=5, sticky='nsew')

    @async_handler
    async def on_run(self):
        input_folder=self.v_folder.get()
        output_folder='output/img'
        raw=False
        correct_light_axis=2
        normalize_brightness=1
        color_map_name='orange-enhanced'
        verbose=0

        self.w_btn_run['state'] = 'disabled'
        output_path = os.path.join(input_folder, output_folder)
        files = sorted(glob(os.path.join(input_folder, '*.[sS][eE][rR]')))
        if len(files) > 0:
            os.makedirs(output_path, exist_ok=True)
        cnt_failed = 0
        cnt_skipped = 0
        cnt_successful = 0
        ts = time.time()
        for i, file in enumerate(files):
            self.v_info.set(_(zh=f'处理中: {i+1}/{len(files)}', en=f'processing: {i+1}/{len(files)}'))
            file_out = os.path.join(output_path, Path(file).stem + '.png')
            if os.path.isfile(file_out):
                print(f'skipped: {file}, output file exists')
                cnt_skipped += 1
                continue
            # print(i, file, file_out)
            try:
                await async_run(ass.raw_file_to_file, file = file, output_file = file_out, raw = raw, correct_light_axis = correct_light_axis, normalize_brightness = normalize_brightness, color_map_name = color_map_name, verbose = verbose)
                cnt_successful += 1
            except Exception as e:
                import traceback
                tk.messagebox.Message(title='error', icon='warning', message=f'{file}\n\n{traceback.format_exc()}').show()
                print(e)
                cnt_failed += 1

        self.v_info.set(_(zh=f'成功: {cnt_successful}, 失败: {cnt_failed}, 跳过: {cnt_skipped}, 耗时: {time.time() - ts:.3f}秒', en=f'done: {cnt_successful}, failed: {cnt_failed}, skipped: {cnt_skipped}, duration: {time.time() - ts:.3f}s'))
        self.w_btn_run['state'] = 'normal'

    def on_about(self):
        # tk.messagebox.Message(title='about', icon='info', message=f'Author: Harold Liang (https://lcsky.org)').show()
        url = 'https://github.com/liangchen-harold/astrospec'
        if sys.platform=='win32':
            os.startfile(url)
        elif sys.platform=='darwin':
            subprocess.Popen(['open', url])
        else:
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print(f'Please open a browser on: {url}')


    def open_folder_selector(self):
        path = tk.filedialog.askdirectory(title="Choose folder contains the .ser files")
        self.v_folder.set(path)

if __name__ == "__main__":
    window = Window()
    async_mainloop(window)
