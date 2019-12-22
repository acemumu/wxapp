function checkForm()
		{
		    var id_list = ['name', 'phone', 'age', 'gender', 'height', 'weight'];
		    var name_dict = {name: "姓名", phone:"手机号码", age:"年龄", gender:"性别", height:"身高", weight:"体重"};
            alert("haha");
            return false;
            alert("请输入{0} ^_^".format(name_dict['name']));
		    for (id_name in id_list)
		    {
		        var value = document.getElementById(id_name).value;
                if (value == "") {
                    alert("请输入{0} ^_^".format(name_dict[id_name]));
                    return false;
		        }
		    }

            var phone = document.getElementById('phone').value;
		    var cardid = document.getElementById('p_cardid').value;
		    var hosp_id = document.getElementById('p_hosp_id').value;

		    if (hosp_id == "" && cardid == "") {
			    alert("身份证与住院号二选一，必须输入一个 ^_^");
			    return false;
			}
			else if (cardid != ""){
			    if (!(/^[1-9]{1}[0-9]{14}$|^[1-9]{1}[0-9]{16}([0-9]|[xX])$/.test(cardid)))
			    {
			        alert("身份证号有误，请重新输入");
			        return false;
		        }
			}

			if (phone != "") {
                if (!(/^1(3|4|5|7|8|9)\d{9}$/.test(phone))) {
                alert("手机号码有误，请重新输入");
                return false;
			}
            return true;
		}

	}


function aaa(){
		var value=document.getElementById("tableType").value;
		var ojobs=document.getElementById("jobs");

		if(value=='0'){
			ojobs.innerHTML="<option>校学生会111</option><option>校学生会222</option><option>校学生会333</option>"
		}else if(value=='1'){
			ojobs.innerHTML="<option>校青志联111</option><option>校青志联222</option><option>校青志联333</option>"
			}else if(value=='2'){
				ojobs.innerHTML="<option>校社联111</option><option>校社联222</option><option>校社联333</option>"
				}else if(value=='3'){
					ojobs.innerHTML="<option>国旗护卫队111</option><option>国旗护卫队222</option><option>国旗护卫队333</option>"
					}else if(value=='4'){
						ojobs.innerHTML="<option>圣兵爱心社111</option><option>圣兵爱心社222</option><option>圣兵爱心社333</option>"
						}


	}