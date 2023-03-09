using System.Text;
IReadOnlyCollection<float> GenerateRandomFloatArray(int n = 4, int numMin = 100, int numMax = 999)
{
    var array = new List<float>();
    var rnd = new Random();

    while (n > 0)
    {
        float numberOne = rnd.Next(numMin, numMax),
                numberTwo = rnd.Next(numMin, numMax);

        var itemNew = numberOne / numberTwo;
        array.Add((float)Math.Round(itemNew, 2));
        n--;
    }

    return array;
}
string GetStringArray(in IReadOnlyCollection<float> array)
{
    var arrOutput = new StringBuilder();

    foreach (var item in array)
    {
        arrOutput.Append(item)
                 .Append(" ");
    }

    return string.Join("; ", array);
}
float GetDiffMinMaxElementsArray(in IReadOnlyCollection<float> array)
    => array.Max() - array.Min();


var arrayRandom = GenerateRandomFloatArray();
var diff = GetDiffMinMaxElementsArray(arrayRandom);
Console.WriteLine($"[{GetStringArray(arrayRandom)}] -> {diff}");