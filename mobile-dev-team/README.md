## Overview
This project lays out an application for Android based on artificial intelligence capable of recognizing the number of roses in an image given by the user, from either the phone's camera or gallery.
## Requirements
- [Android Studio](https://developer.android.com/studio) version Artic Fox 2020.3.1 Patch 3 or greater (for cloning and editing the app)
- Android 6.0 Marshmallow or greater (for installing and testing in an Android phone)
## Screenshots
     
|        Home Screen               |       Test Images                |         Gallery Permissions      |       Gallery Functionality      | 
:---------------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------------:
|![Alt text](./assets/App%20(1).jpg)|![Alt text](./assets/App%20(2).jpg)|![Alt text](./assets/App%20(3).jpg)|![Alt text](./assets/App%20(4).jpg)|

| Inference with Gallery Image     |       Camera Permissions         |       Camera Functionality       |    Inference with Camera Image   | 
:---------------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------------:
|![Alt text](./assets/App%20(5).jpg)|![Alt text](./assets/App%20(6).jpg)|![Alt text](./assets/App%20(7).jpg)|![Alt text](./assets/App%20(8).jpg)|

## Importing the Project on Android Studio
1. Clone or download the **main repository** (Check the main repository [README](https://github.com/Leo-Thomas/Yachay-Tech-object-detection-projects/blob/main/README.md) for instructions)
2. Open Android Studio
3. Click on File -> New -> Import Project
     - **First Time using Android Studio:** Click Open an existing Android Studio project
4. Search for the directory `Yachay-Tech-object-detection-projects/mobile-dev-team` and select it.
5. If you get a Gradle Sync popup, click OK and wait for it to sync.

## Installation

### Install using Android Studio
1. Configure your phone to connect to Android Studio and build the app. See https://developer.android.com/studio/run/device for details.
2. Connect yout phone to your computer (with an USB cable or through Wi-Fi depending on how you configured your phone).
3. If everything was done correctly, you will see your phone's model name on the panel near the upper right corner.
     ![Model Name](./assets/model_name.png)
4. You can then install and run the app by selecting Run -> Run 'app', or by clicking the green play button right to your phone's model name. Don't disconnect your phone until the app is loaded.

### Install using the APK
1. Search the file MDT.Rose.Counter.apk in `Yachay-Tech-object-detection-projects/mobile-dev-team/apk`.
2. Copy the apk to your phone.
3. In your phone, search for the apk and install it. If your phone asks for confirmation or permission to install the apk, accept.

## How to change the AI model
In case you want to test the app using your own TFLite model you just need to replace the `model.tflite` file in `Yachay-Tech-object-detection-projects/mobile-dev-team/app/src/main/assets`. The model can be generated and trained following [this](https://github.com/Leo-Thomas/Yachay-Tech-object-detection-projects/tree/main/AI-Team#training) instructions. If you need to change the detection threshold for the model, do it in line 182 of `app/java/org.tensorflow.codelabs.objectdetection/MainActivity.kt` in Android Studio, inside `.setScoreThreshold()`. You can then compile/run the app again in Android Studio, or generate a new apk by clicking Build -> Build Bundle(s)/APK(s) -> Build APK(s). The apk will be stored in `Yachay-Tech-object-detection-projects/mobile-dev-team/app/build/outputs/apk/debug/`, as `app-debug.apk`.

## Usage
Make sure the app is already installed in your phone.
1. Find the application on your cell phone and open it.
2. Tap **Take Photo** to take a photo using your phone's camera or **Gallery** to choose a photo from your phone's gallery. Only for the first time, give the permisions to access gallery or camera and tap the corresponding button again. Alternatively, you can touch the sample photos above the buttons to select them.
3. The inference of the image will be done automatically, and the result will be shown in the center of the screen.
4. You can then save the image using the **Save Result** button or start a new inference by repeating step 2. The photos saved from the app are stored in the Pictures/Inferences folder from your phone's internal storage.

## Authors of this project
- Stadyn Román - stadyn.roman@yachaytech.edu.ec - [LinkedIn](https://www.linkedin.com/in/stadyn/)
- Argenis Andrade - argenis.andrade@yachaytech.edu.ec - [LinkedIn](https://www.linkedin.com/in/argenisraz/) 
- Jefferson Chipantasig - jefferson.chipantasi@yachaytech.edu.ec - [LinkedIn](https://www.linkedin.com/in/javec/)
- Jaime Astudillo - jaime.astudillo@yachaytech.edu.ec - [LinkedIn](https://www.linkedin.com/in/jaime-astudillo-664754228/)

## Link to the repository containing only this project

https://github.com/StadynR/object-detection-soft-eng

## External Libraries and Repositories Used
- [ImagePicker](https://github.com/Dhaval2404/ImagePicker)
- [On-device Machine Learning Codelabs](https://github.com/googlecodelabs/odml-pathways)
