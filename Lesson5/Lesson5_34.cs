using System.Text;
IReadOnlyCollection<int> GenerateRandomIntArray(int n = 4, int numMin = 100, int numMax = 999)
{
    var array = new List<int>();
    var rnd = new Random();

    while (n > 0)
    {
        int itemNew = rnd.Next(numMin, numMax);
        array.Add(itemNew);
        n--;
    }

    return array;
}
string GetStringArray(in IReadOnlyCollection<int> array)
{
    var arrOutput = new StringBuilder();

    foreach (var item in array)
    {
        arrOutput.Append(item)
                 .Append(" ");
    }

    return string.Join(",", array);
}
int CountEvenNumbers(IReadOnlyCollection<int> numbers)
    => numbers.Where(num => num % 2 == 0)
              .Count();


var arrayRandom = GenerateRandomIntArray();
var countPositiveNums = CountEvenNumbers(arrayRandom);
Console.WriteLine($"[{GetStringArray(arrayRandom)}] -> {countPositiveNums}");