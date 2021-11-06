const getFrac = (num) => Number('0.' + String(num).split('.')[1]); // Функция для выделения дробной части из десятичного числа
const getWhole = (num) => Number(String(num).split('.')[0]); // Функция для выделения целой части из десятичного числа

const toBinWhole = (whole) => { // Фукнция для перевода целой части в двоичную систему
  const bin = []; // Массив, в который добавляем остатки от деления.
  while(whole >= 1) { // Пока число не меньше двух
    bin.push(parseInt(whole % 2)); // Добавляем остаток
    whole = parseInt(whole / 2); // Делим число
  };
  bin.reverse(); // Переворачиваем массив
  return bin.join(''); // Записываем все числа в строку
};

const toBinFractional = (frac) => { // Фукнция для перевода дробной части
  const bin = []; // Массив, в который добавляем целые части умножения
  for(let i = 0; i < 10; i++) { // Я сделал преобразование до 10 знаков чтобы не было слишком много чисел
    frac = frac * 2; // Умножаем дробную часть на 2
    bin.push(getWhole(frac)); // Выделяем целую часть и добавляем в результирующий массив
    frac = getFrac(frac); // Отбрасываем целую часть
  };
  return bin.join('');
};

const toBin = (num) => { // Функция для перевода всего числа
  num = num.replace(',', '.'); // Заменяем запятую на точку чтобы не было ошибки
  const whole = getWhole(num); // Выделяем целую часть
  const frac = getFrac(num); // Выделяем дробную часть
  if(!frac) { // Если дробной части нет
    return toBinWhole(whole); // То преобразуем целую часть и возвращаем ее
  };
  return ([toBinWhole(whole), toBinFractional(frac)].join('.'));
  /*
     Преобразуем целую и дробную части,
     добавляем их в массив и объединяем по символу '.',
     получив запись числа в двоичной системе
  */
};

var readline = require('readline'); // Модуль для работы с консолью

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


rl.question("Enter num: ", (input) => { // Читаем из консоли число и преобразуем
  console.log(toBin(input));
  rl.close();
});
