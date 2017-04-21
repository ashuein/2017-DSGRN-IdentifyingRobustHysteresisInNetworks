for file in `ls -I '*.*' networks`; do

  echo "Network:"
  echo $file

  echo "Number of reduced parameter indices = "
  python NumReducedParameterIndex.py networks/$file

  ./collate.sh computations/$file

  echo "Number of hysteresis matches = "
  echo `wc -w "computations/${file}_hysteresis.txt"`

  echo "Number of resettable bistability matches = "
  echo `wc -w "computations/${file}_resettable.txt"`

  echo " "
done
