# SentiPers: A Sentiment Analysis Corpus for Persian

<div dir="rtl">
توسعه پیکره سنتی پرس حدودا از سال ۱۳۹۳ در گروه پردازش زبان طبیعی دانشگاه گیلان آغاز شد. داده های اولیه و خام سنتی پرس از وبسایت دیجی کالا استخراج و پس از دسته بندی در قالب اسناد و جملات، توسط گروهی از دانشجویان مهندسی کامپیوتر دانشگاه گیلان به صورت دستی نشانه گذاری شدند.

سنتی پرس از زمان ایجاد تاکنون به صورت رایگان و با دریافت درخواست از طریق ایمیل برای همگان در دسترس بود. با وجود اینکه در طول این سالها سنتی پرس تحت گسترش و توسعه فعال نبوده و در سالهای اخیر شاهد رشد چشمگیری در تحقیقات در زمینه پردازش زبان فارسی و به ویژه تحلیل احساس، و معرفی انواع متنوعی از ابزارها و منابع بوده ایم، این پیکره همچنان به عنوان یک منبع مفید و با تعداد داده های مناسب و برچسب های منحصر به فرد مورد استفاده قرار گرفته و میتواند بگیرد.

هدف از ایجاد این مخزن، آسان سازی هر چه بیشتر دسترسی به سنتی پرس بوده است. دریافت درخواستهای متعدد از طریق ایمیل از دانشگاههای مختلف ما را بر آن داشت که این مجموعه را کاملا عمومی کنیم. در ادامه سعی کرده ایم که اطلاعات مورد نیاز برای استفاده از منابع و فایلهای موجود در این مخزن را به شیوه مناسب مستندسازی کنیم. همچنین میدانیم و کاملا آگاه هستیم که همیشه احتمال وجود خطا در برخی از برچسب های بار معنایی وجود دارد، به همین دلیل سعی کردیم با فراهم کردم یک سری امکانات (توضیحات مقتضی در ادامه و به زبان انگلیسی آمده، سعی میکنیم که توضیحات کاملتری به زبان فارسی هم تهیه نماییم)، ویرایش برچسب های بار معنایی را نیز میسر نماییم.

از تمامی علاقمندان دعوت میکنیم که برای بهتر شدن این مجموعه ما را همیاری کنند. بهتر شدن سنتی پرس به عنوان یک منبع رایگان در نهایت میتواند در بسیاری از تحقیقات مربوط به تحلیل احساس در زبان فارسی یاریگر همگان باشد.
</div>

------------
**SentiPers** is one of the first corpora developed for Sentiment Analysis in Persian. Documents in SentiPers are manually annotated at different levels. We not only assigned polarity labels to sentences and documents but also annotated pairs of `target` and `opinion` words in them (e.g. in "This phone is really good", "phone" and and "really good" are `target` and `opinion` word, respectively). 

In the version published in this repository, there are more than `15,500` unique sentences with polarity labels in the range of `["-2", "-1", "0", "+1", "+2"]` with `-2` being `very negative`, `+2` being `very positive`, and `0` being `neutral`.

### Repository files
All the SentiPers files are located in the `data` folder:
* `data`
  * `main` original files of SentiPers that we made publicly available in XML format.
  * `extra` extra files in a different format than the XML files in the `main` folder. These are the files we decided to make public after publishing the original files.
  * `sentipers.xlsx` a single excel file that includes all the unique sentences from `main` and `extra` folders. We have included methods in `sentipers.py` to generate this file, in case you want to remove the file and have a fresh copy.


We have also included two jupyter notebooks in this repository:
* `demo.ipynb` in this notebook, we have demonstrated how you can use the methods in `sentipers.py`
* `modify.ipynb` in this notebook, we have shown how you can modify SentiPers entries. The main purpose of including such a notebook is modifying the polarity labels that may have incorrectly assigned to some sentences.

### Requirements
* You need to install `pandas` to use methods in `sentipers.py`. Detailed instruction to install `pandas` can be found [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).
* **Important:** You also need to install `qgrid` if you want to use the `modify.ipynb` to update SentiPers. Instructions for installing `qgrid` can be found [here](https://github.com/quantopian/qgrid). `qgrid` is a widget for interactively working (editing) data frames in jupyter notebook.
* You can also use the following command to install all the requirements: ```pip install -r requirements.txt```


### How to cite `SentiPers`:

If you found [SentiPers](https://arxiv.org/abs/1801.07737) useful or used it in your work, please use the following information to cite our paper:
```bibtex
@article{hosseini2018sentipers,
  title={SentiPers: A sentiment analysis corpus for Persian},
  author={Hosseini, Pedram and Ramaki, Ali Ahmadian and Maleki, Hassan and Anvari, Mansoureh and Mirroshandel, Seyed Abolghasem},
  journal={arXiv preprint arXiv:1801.07737},
  year={2018}
}
```

### How to contribute to SentiPers:
We welcome and appreciate any contribution to SentiPers to make it a better publicly available resource for Natural Language Processing and Sentiment Analysis. Feel free to reach out to [Pedram Hosseini](mailto:pdr.hosseini@gmail.com) if you have any suggestion/idea. We will also be happy to review your pull requests if you think any changes can be made to the SentiPers or helper methods in `sentipers.py`.
