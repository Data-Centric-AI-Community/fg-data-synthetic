`ydata-synthetic` is available through PyPi, allowing an easy process of installation and integration with the data science programming environments (Google Colab, Jupyter Notebooks, Visual Studio Code, PyCharm) and stack (`pandas`, `numpy`, `scikit-learn`).

## Installing the package

Currently, the package supports **Python versions 3.9 through 3.11**, and can be installed in Windows, Linux, or MacOS operating systems.

Prior to the package installation, it is recommended to create a virtual or `conda`/`mamba` environment:

=== "conda"
    ``` commandline
    conda create -n synth-env python=3.10
    conda activate synth-env
    ```

=== "mamba"
    ``` commandline
    mamba create -n synth-env python=3.10
    mamba activate synth-env
    ```

The above commands create and activate a new environment called "synth-env" with Python version 3.10.X. In the new environment, you can then install `ydata-synthetic`:

=== "pypi"
    ``` commandline
    pip install ydata-synthetic
    ```
    To install a specific version (e.g., the latest stable version v1.4.0), use:
    ``` commandline
    pip install ydata-synthetic==1.4.0
    ```

:fontawesome-brands-youtube:{ style="color: #EE0F0F" }
[Installing ydata-synthetic](https://www.youtube.com/watch?v=aESmGcxtBdU) – :octicons-clock-24:
5min – Step-by-step installation guide

## Verification

After installation, verify the installed version with:

```python
import ydata_synthetic
print(ydata_synthetic.__version__)
```

## Using Google Colab

To install inside a Google Colab notebook, you can use the following:

``` commandline
!pip install ydata-synthetic
```

Make sure your Google Colab is running Python versions `>=3.9, <3.12`. Learn how to configure Python versions on Google Colab [here](https://stackoverflow.com/questions/68657341/how-can-i-update-google-colabs-python-version/68658479#68658479).

## Installing the Streamlit App

Since version 1.0.0, the `ydata-synthetic` includes a GUI experience provided by a Streamlit app. The UI supports the data synthesization process from reading the data to profiling the synthetic data generation, and can be installed as follows:

``` commandline
pip install "ydata-synthetic[streamlit]"
```

Note that Jupyter or Colab Notebooks are not yet supported, so use it in your Python environment.

### Launching the App

To launch the Streamlit app after installation, run the following in your Python environment:

```python
import ydata_synthetic.streamlit_app as streamlit_app
streamlit_app.run()
```

:fontawesome-brands-youtube:{ style="color: #EE0F0F" }
[How to launch the Streamlit GUI](https://www.youtube.com/watch?v=YOUR_STREAMLIT_GUIDE_LINK) – :octicons-clock-24:
Quick guide to starting the Streamlit app

<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=dd69a9f9-0901-4cb4-9e56-b1e69877dca1" />

