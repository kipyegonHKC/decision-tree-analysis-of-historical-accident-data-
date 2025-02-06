import jpype
import jpype.imports
from jpype.types import JString


weka_jar_path = "path/to/weka.jar"  
jpype.startJVM(classpath=[weka_jar_path])


from weka.core.converters import ConverterUtils
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random


data_file = "path/to/your/datafile.arff"
loader = ConverterUtils.DataSource(data_file)
data = loader.getDataSet()


if data.classIndex() == -1:
    data.setClassIndex(data.numAttributes() - 1)


classifier = Classifier(classname="weka.classifiers.trees.J48")


evaluation = Evaluation(data)
evaluation.crossValidateModel(classifier, data, 10, Random(1))


print("=== Classifier Model ===")
print(classifier.toString())
print("\n=== Evaluation Results ===")
print(evaluation.toSummaryString())
print(evaluation.toClassDetailsString())
print(evaluation.toMatrixString())


model_file = "j48_model.model"
serialization_helper = jpype.JClass("weka.core.SerializationHelper")
serialization_helper.write(JString(model_file), classifier)

print(f"Model saved to {model_file}")


jpype.shutdownJVM()
