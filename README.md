# Vitiligo-Prediction-Using-ML

Support vector machine is a supervised machine learning algorithm primarily used for classification and regression tasks. Its primary objective is to find a hyperplane that best separates data points of different classes in a feature space. 

The following outlines the sequential actions undertaken during the project's execution:

1. Google Colaboratory was employed to configure and train the SVM model, utilizing the vitiligo dataset in CSV format. In this notebook, essential libraries were imported, followed by the loading and analysis of the dataset from the "vitiligo.csv" file. Subsequently, the dataset underwent preprocessing and was divided into training and test data, maintaining an 80:20 ratio.

2. Following step 1, a Support Vector Machine (SVM) classifier employing a linear kernel is initialized and trained using the provided training data. Subsequently, the accuracy of the trained model is assessed on both the training and testing datasets. Finally, the trained model is preserved to a file "trained_model.sav" using the pickle library.

3. A specialized Anaconda environment is established for the project, within which the pickle and Streamlit packages are installed to facilitate further development.

4. Constructed a web application using the Streamlit tool within the Spyder IDE. This application utilizes the pre-trained model, which was originally obtained from Google Colab, as detailed in the "vitiligo_prediction.py" script.

5. Launched the web application locally by entering the command "streamlit run C:\User........\vitiligo_prediction.py" in the Anaconda terminal of the designated environment, effectively executing the Spyder Python file.

   ![Streamlit](https://github.com/sanjana459/Vitiligo-Prediction-Using-ML/assets/85347345/cee05601-c3dd-43d5-97fb-48489851de01)


   ![Anaconda](https://github.com/sanjana459/Vitiligo-Prediction-Using-ML/assets/85347345/3b844151-6fea-4e8c-a4a7-dc0ec88c7883)

   

