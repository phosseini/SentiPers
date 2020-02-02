# SentiPers: A Sentiment Corpus for Persian

SentiPers is one of the first corpora developed for Sentiment Analysis in Persian. Documents in SentiPers are manually annotated in different levels. We not only assigned polarity labels to sentences and documents, but also annotated pairs of `target` and `opinion` (e.g. in "This phone is really good", "phone" is a `target` and "really good" is an `opinion`). 

In current version published in this repository, there are more than `15,500` unique sentences with polarity labels in the range of `["-2", "-1", "0", "+1", "+2"]` with `-2` being `very negative`, `+2` being `very positive`, and `0` being `neutral`.

SentiPers was developed a while ago (around 2014) and is not under active expansion or development. We are aware of the fact that since creating SentiPers, there have also been other Sentiment corpora developed for Persian, however, we still believe SentiPers is a rich resource that can be extremely useful in different hypothesis testing in research around Sentiment Analysis in Persian.

### Repository files
All the SentiPers files are located in the `data` folder:
* `data`
  * `main` original files of SentiPers that we made publicly available in XML format.
  * `extra` extra files in a different format than the XML files in `main` folder. These are those files we decided to make public after publishing the original files.
  * `sentipers.xlsx` a single excel file that includes all the unique sentences from `main` and `extra` folders. We have included methods in `sentipers.py` to generate this file, in case you want to remove the file and have a fresh version.


We have also included two jupyter notebook in this repository:
* `demo.ipynb` in this notebook, we have demonstrated how you can use the methods in `sentipers.py`
* `modify.ipynb` in this notebook, we have shown how you can modify SentiPers entries. The main purpose of including such a notebook is modifying the polarity labels that may have incorrectly assigned to some sentences.


### Contributions
Even though we are not actively expanding or developing SentiPers, but we welcome and appreciate any contribution to SentiPers to make it a better resource for Persian Natural Language Processing. Feel free to reach out to [Pedram Hosseini](mailto:pdr.hosseini@gmail.com) if you have any suggestion/idea. We will also be happy to review your pull request if you think any changes can be made to the SentiPers or helper methods in `sentipers.py`. 

### Next steps:
* I try to add more explanations in Persian for those who might prefer to read instructions in that language.
* I'll be also adding helper methods to extract the `(target, opinion)` tag pairs from sentences that are also annotated in SentiPers.
