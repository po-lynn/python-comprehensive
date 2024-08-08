// function positiveSum(arr) {
//     return arr.reduce((a,b)=> a + (b > 0 ? b : 0),0);
// }
//  console.log(positiveSum([1,-2,7]))

//  makeNegative(1); // return -1
//  makeNegative(-5); // return -5
//  makeNegative(0); //return 0
//  makeNegative(0.12); //return -0.12

// function solution(str){
//     return str.split('').reverse().join('');  
//   }
//  console.log(solution("hello")); 

// function consecutiveDuplicate(strs) {
//   let new_str = strs.split(""); // gives array of type string
//   let count = 1;
//   let result = "";

//   for(let i = 0; i < new_str.length; i++) {
//       if(new_str[i] === new_str[i + 1]) {
//           count++;
//       } else {
//           result += new_str[i] + count;
//           count = 1;
//       }
//   }
//   return result
// }

// console.log(consecutiveDuplicate("aaabcccddb"));

// function solution(arr){
//         let sum =0;
//         for(let i=0; i< arr.length;i++){
//             if(arr[i]<0)
//               sum= 0;
//             else sum = sum+ arr[i]
//         }
//         return sum;
//       }
//       console.log(solution([1,2,-3,4]))

function repeatStr(time,str){
  let newstring = '';
  for (let n=0;n<time;n++){
    newstring = newstring + str;
  }
  return newstring;
}
console.log(repeatStr(2,'hello'));