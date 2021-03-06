<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header('Access-Control-Allow-Headers: Origin, Content-Type, Authorization, X-Auth-Token');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS');
header('Content-Type: text/html; charset=utf-8');
include "db.php";
$param = file_get_contents("php://input"); 
$data = json_decode($param);
$sql = "";

if (isset($data->what)) { 

    switch ($data->what) {
        
        // excute string query
        case 0: {
            $sql = $data->sql;
            break;
        }

        //******************tf_staff************************
        // tf_staff(id,name,name_id,branch_id,phone,email,address,hair_samples,image_url,level_id,cat_toc,goi_dau,user_id,time,last_time_update,password)
        // Get all data from tf_staff
        case 10: {
            $sql = "SELECT * FROM tf_staff";
            break;
        }

        // Insert data to tf_staff
        case 11: {
            $sql = "INSERT INTO tf_staff(name,name_id,branch_id,phone,email,address,hair_samples,image_url,level_id,cat_toc,goi_dau,user_id,time,last_time_update,password)
            		VALUES('$data->name','$data->name_id','$data->branch_id','$data->phone','$data->email','$data->address','$data->hair_samples','$data->image_url','$data->level_id','$data->cat_toc','$data->goi_dau','$data->user_id','$data->time','$data->last_time_update','$data->password')";
            break;
        }

        // Update data tf_staff
        case 12: {
            $sql = "UPDATE tf_staff SET name='$data->name', name_id='$data->name_id', branch_id='$data->branch_id', phone='$data->phone', email='$data->email', address='$data->address', hair_samples='$data->hair_samples', image_url='$data->image_url', level_id='$data->level_id', cat_toc='$data->cat_toc', goi_dau='$data->goi_dau', user_id='$data->user_id', time='$data->time', last_time_update='$data->last_time_update', password = '$data->password'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of tf_staff
        case 13: {
            $sql = "DELETE FROM tf_staff
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id tf_staff
        case 14: {
            $sql = "SELECT * FROM tf_staff
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id tf_staff cắt tóc
        case 15: {
            $sql = "SELECT * FROM tf_staff
            		WHERE cat_toc='1' AND branch_id = '2' ";
            break;
        } 

        // Find data with id tf_staff gội đầu
        case 16: {
            $sql = "SELECT * FROM tf_staff
            		WHERE cat_toc='0' AND branch_id = '2' ";
            break;
        } 


        //******************tf_booking************************
        // tf_booking(id,branch_id,phone,name,appointment_time,appointment_timestamp,time_slot,staff_id,staff_id_goi_dau,services,service_ids,price,price_discount,discount,is_other,price_other,note,status,user_change,time,time_change)
        // Get all data from tf_booking
        case 20: {
            $sql = "SELECT * FROM tf_booking";
            break;
        }

        // Insert data to tf_booking
        case 21: {
            $sql = "INSERT INTO tf_booking(branch_id,phone,name,appointment_time,appointment_timestamp,time_slot,staff_id,staff_id_goi_dau,services,service_ids,price,price_discount,discount,is_other,price_other,note,status,user_change,time,time_change)
            		VALUES('$data->branch_id','$data->phone','$data->name','$data->appointment_time','$data->appointment_timestamp','$data->time_slot','$data->staff_id','$data->staff_id_goi_dau','$data->services','$data->service_ids','$data->price','$data->price_discount','$data->discount','$data->is_other','$data->price_other','$data->note','$data->status','$data->user_change','$data->time','$data->time_change')";
            break;
        }

        // Update data tf_booking
        case 22: {
            $sql = "UPDATE tf_booking SET branch_id='$data->branch_id', phone='$data->phone', name='$data->name', appointment_time='$data->appointment_time', appointment_timestamp='$data->appointment_timestamp', time_slot='$data->time_slot', staff_id='$data->staff_id', staff_id_goi_dau='$data->staff_id_goi_dau', services='$data->services', service_ids='$data->service_ids', price='$data->price', price_discount='$data->price_discount', discount='$data->discount', is_other='$data->is_other', price_other='$data->price_other', note='$data->note', status='$data->status', user_change='$data->user_change', time='$data->time', time_change = '$data->time_change'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of tf_booking
        case 23: {
            $sql = "DELETE FROM tf_booking
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id tf_booking
        case 24: {
            $sql = "SELECT * FROM tf_booking
            		WHERE id='$data->id'";
            break;
        } 


        //******************tf_branch************************
        // tf_branch(id,name,user_id,time,last_time_update)
        // Get all data from tf_branch
        case 30: {
            $sql = "SELECT * FROM tf_branch";
            break;
        }

        // Insert data to tf_branch
        case 31: {
            $sql = "INSERT INTO tf_branch(name,user_id,time,last_time_update)
            		VALUES('$data->name','$data->user_id','$data->time','$data->last_time_update')";
            break;
        }

        // Update data tf_branch
        case 32: {
            $sql = "UPDATE tf_branch SET name='$data->name', user_id='$data->user_id', time='$data->time', last_time_update = '$data->last_time_update'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of tf_branch
        case 33: {
            $sql = "DELETE FROM tf_branch
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id tf_branch
        case 34: {
            $sql = "SELECT * FROM tf_branch
            		WHERE id='$data->id'";
            break;
        }


        //******************tf_product************************
        // tf_product(id,name,price,discount,user_id,time,last_time_update)
        // Get all data from tf_product
        case 40: {
            $sql = "SELECT * FROM tf_product";
            break;
        }

        // Insert data to tf_product
        case 41: {
            $sql = "INSERT INTO tf_product(name,price,discount,user_id,time,last_time_update)
            		VALUES('$data->name','$data->price','$data->discount','$data->user_id','$data->time','$data->last_time_update')";
            break;
        }

        // Update data tf_product
        case 42: {
            $sql = "UPDATE tf_product SET name='$data->name', price='$data->price', discount='$data->discount', user_id='$data->user_id', time='$data->time', last_time_update = '$data->last_time_update'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of tf_product
        case 43: {
            $sql = "DELETE FROM tf_product
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id tf_product
        case 44: {
            $sql = "SELECT * FROM tf_product
            		WHERE id='$data->id'";
            break;
        }


        //******************tf_service************************
        // tf_service(id,name,name_id,description,position,publish,price,price_discount,start_time,end_time,user_id,time,last_time_update)
        // Get all data from tf_service
        case 50: {
            $sql = "SELECT * FROM tf_service";
            break;
        }

        // Insert data to tf_service
        case 51: {
            $sql = "INSERT INTO tf_service(name,name_id,description,position,publish,price,price_discount,start_time,end_time,user_id,time,last_time_update)
            		VALUES('$data->name','$data->name_id','$data->description','$data->position','$data->publish','$data->price','$data->price_discount','$data->start_time','$data->end_time','$data->user_id','$data->time','$data->last_time_update')";
            break;
        }

        // Update data tf_service
        case 52: {
            $sql = "UPDATE tf_service SET name='$data->name', name_id='$data->name_id', description='$data->description', position='$data->position', publish='$data->publish', price='$data->price', price_discount='$data->price_discount', start_time='$data->start_time', end_time='$data->end_time', user_id='$data->user_id', time='$data->time', last_time_update = '$data->last_time_update'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of tf_service
        case 53: {
            $sql = "DELETE FROM tf_service
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id tf_service
        case 54: {
            $sql = "SELECT * FROM tf_service
            		WHERE id='$data->id'";
            break;
        } 

        
    }
    
    // echo $sql."<br>";
    
    //excute sql 
    $result = $conn->query($sql);
    
    // echo json_encode($result);
    if (isset($result->num_rows) && ($result->num_rows > 0)) {
        // output data of each row
        // echo "for";
        $data = array();
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }

        echo json_encode($data);
    } else {
        // echo json_encode($result);
        echo "null";
    }
}
$conn->close();
?>