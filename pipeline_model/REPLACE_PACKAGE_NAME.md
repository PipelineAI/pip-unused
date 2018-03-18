```
find . -name "*.py" -print0 | xargs -0 sed -i '' -e 's/from tensorflow/from pipeline_model.tensorflow/g'
```
