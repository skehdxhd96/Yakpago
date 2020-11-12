var medicine_names = new Array();

//입력페이지 Dynamic Select box 구현을 위한 javascript 함수
function insertSubcategories() {
    var category_select = document.getElementById('input_category');
    var subcategory_select = document.getElementById('input_subcategory');

    var category = category_select.value;
    
    fetch ('/subcategory/' + category).then(function(response) {
        response.json().then(function(data) {
        let optionHTML = '';
        optionHTML += "<option value='subcategory_all'>모두 선택" + "</option>";
        for (let subcategory of data) {
            optionHTML += "<option value='" + subcategory.subcategory + "'>" + subcategory.subcategory + "</option>";
        }
        subcategory_select.innerHTML = optionHTML;
        });
    });
}

//입력페이지 약품명 검색하여 약품 이름을 프론트에서 표로 보여주는 javascript 함수
document.getElementById('search_medicine').onclick = function() {
    let input_medicine = document.getElementById('input_medicine').value;
    let medicine_table = document.getElementById('medicine_table');

    fetch('/input/' + input_medicine).then(function(response) {
        response.json().then(function(data) {
            let index = 1;
            let optionHTML = '';
            for (let medicine of data) {
                optionHTML += "<tr> <th scope='row'>" + index + "</th> <td class='td_medicine' value='" + medicine + "'>" + medicine + "</td> </tr>";
                index += 1;
            }
            medicine_table.innerHTML = optionHTML;
        });
    });
    
    return false;
}

//입력페이지 약품명 입력 부분 동적 이벤트 구현 함수(+form input 태그에 약품 이름 넣어주는 함수).
document.getElementById('medicine_table').onmouseover = function() {
    let td_medicines = document.getElementsByClassName('td_medicine');

    for (let i=0; i<td_medicines.length; i++) {
        td_medicines[i].onclick = function() {
            if (this.style.backgroundColor == "") {
                this.style.backgroundColor = '#5cb85c';
                this.style.color = 'white';
                medicine_names.push(this.outerText);
            }
            else {
                this.style.backgroundColor = '';
                this.style.color = 'black';
                const index = medicine_names.indexOf(this.outerText);
                if (index > -1) 
                    medicine_names.splice(index, 1);
            }
        }
    }
    document.getElementById('input_ingredients').value = medicine_names;
}

function check(val, re) {
    if(re.test(val)) {
        return true;
    }
    else {
        return false;
    }
}

//입력페이지 체중값 유효성 검사 함수
document.getElementById('input_weight').onkeyup = function() {
    let input_age = document.getElementById('input_weight');

    if (!check(input_age.value, /[0-9]/)) {
        document.getElementById('weigt_reg').style.display = "block";
    }
    else {
        document.getElementById('weigt_reg').style.display = "none";
    }
};

//입력페이지 submit 버튼 클릭했을 때 유효성 검사 후 에러를 alert하고 에러입력텍스트로 focus 하는 함수.
document.getElementById('input_page_button').onclick = function() {
    let input_age = document.getElementById('input_age');
    let input_weight = document.getElementById('input_weight')
    medicine_names = [];
    if (input_weight.value=="") {
        alert("체중은 필수 사항입니다.");
        input_weight.focus();
        return false;
    }
    if (input_weight.value!="" & !check(input_weight.value, /[0-9]/)) {
        alert("체중은 숫자만 입력 가능합니다.")
        input_weight.focus();
        return false;
    }
};

//결과페이지 추천 약품 모델을 보여주는 함수.(페이지 로딩 첫 화면)
window.onload = function() {
    fetch('/result').then(function(response) {
        response.json().then(function(data) {
            for (let i=3; i<6; i++) {
                document.getElementsByClassName('panel-heading')[i%3].getElementsByTagName('p')[0].innerHTML = data[i].item_name;
            }
        });
    });
    
    return false;
}