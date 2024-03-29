const f_split = (line, char) => {
  const result = []; // Результирующий массив
  let for_search = ''; // Переменная для поиска символов
  for(let i in line) { // Гоним строку циклом
    if((line[i] == char)) { // Если наткнулись на символ-разделитель
      if(for_search) { // Если до этого нашли какие-то символы
        result.push(for_search); // Добавляем их в массив
        for_search = ''; // И обнуляем поисковую переменную
      };
      continue;  // Если до этого ничего не нашли, то просто пропускаем итерацию
    };
    for_search += line[i]; // Прибавляем в поисковую переменную все, что не является символом-разделителем
  };
  result.push(for_search); // После завершения цикла добавляем в массив остатки символов
  return result;
};

const f_map = (obj, func) => {
  const result = [];
  for(let i of obj) {
    result.push(func(i));
  };
};

const f_filter = (obj, func) => {
  const result = [];
  for(let i of obj) {
    if(func(i)) {
      result.push(i);
    };
  };
  return result;
};

function f_reduce(arr, callback, result) {
  /* arr - перебираемый массив
     callback - переданная функция,
     result - "аккумулятор"

     Проверяем, существует ли результат.
     Если нет, им становится первый элемент массива
     Применяем переданную функцию к каждому элементу массива
     возвращаем результат
  */
  let i = 0;
  if (arguments.length < 3) {
    i = 1;
    result = arr[0];
  }
  for (; i < arr.length; i++) {
    result = callback(result, arr[i], i, arr);
  }
  return result;
}

const f_sum = (obj) => {
  let sum = 0; // Переменная для суммы
  for(const i of obj) { // Просто суммируем значения в цикле
    sum += Number(i);
  };
  return sum;
};

const line = "100 200      3 5 6 999";
console.log(f_sum(f_split(line, ' ')));
