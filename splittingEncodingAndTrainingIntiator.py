from ExceptionLoggerAndUtils.exception import CustomException
from ExceptionLoggerAndUtils.logger import App_Logger
from Source.dataSplittingTransformationAndTraining.dataSplittingTransformation import dataSplittingTransformationClass
from Source.dataSplittingTransformationAndTraining.modelTraining import ModelTrainerClass

from ExceptionLoggerAndUtils.utils import save_object
import os
import sys
import pandas as pd


class splittingAndTrainingClass():
    def __init__(self):
        self.dataSplittingTransformationC = dataSplittingTransformationClass()
        self.ModelTrainerClass = ModelTrainerClass()
        self.File_Path = "cleanedData/cleanedDataFile.csv"
        self.transformationFilePath = os.path.join('artifacts',"transformation.pkl")


    def splittingAndTrainingMethod(self):
        try:
            X_train, X_test, y_train, y_test = self.dataSplittingTransformationC.dataReadingAndSpliting(self.File_Path)
            transformationOfData =self.dataSplittingTransformationC.dataTransformation()
            print(pd.DataFrame(X_train.T))
            X_train = transformationOfData.fit_transform(X_train)
            X_test = transformationOfData.transform(X_test)
            print(X_train.T)

            save_object(
                file_path= self.transformationFilePath,
                obj = transformationOfData
            )

            models,params = self.ModelTrainerClass.modelsToTrainAndParameters()
            self.ModelTrainerClass.modelTraingMethod(X_train, X_test, y_train, y_test,models,params)

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    splittingAndTrainingClassObj = splittingAndTrainingClass()
    splittingAndTrainingClassObj.splittingAndTrainingMethod()