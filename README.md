# Instagram Reel Downloader

This is a Python application that allows you to download Instagram Reels using their URLs. The application provides a dark-themed graphical user interface (GUI) built with Tkinter and ttk.

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3.x: You can download Python from the official website: https://www.python.org/downloads/
- Install the required dependencies by running the following command:
pip install -r requirements.txt


## Installation

1. Clone the repository or download the code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required dependencies by running the command mentioned above.

## Usage

To run the application, execute the following command in the project directory:


The application window will open. Follow these steps to download an Instagram Reel:

1. Enter the URL of the Instagram Reel in the provided field.

2. Click the "Download Reel" button.

3. The reel will be downloaded to a folder named "<username>_reels" in the current directory.

4. Once the download is complete, the status label will show "Download complete!".

Note: The application assumes the URL provided is a valid Instagram Reel URL. If an invalid URL is entered, an error message will be displayed.

## Customization

You can customize the GUI theme by modifying the code in the `download_reel` function. The `style.configure` calls allow you to change the background and foreground colors of various elements.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
