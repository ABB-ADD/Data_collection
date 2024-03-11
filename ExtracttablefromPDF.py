

def ExtracttablefromPDF(Output_path,Img_path):
    import os
    import cv2
    from datetime import datetime
    from paddleocr import PPStructure,draw_structure_result,save_structure_res
    from Batch_read import Barch_read
    from time import sleep

    starttime = datetime.now()
    table_engine = PPStructure(show_log=True,lang='en', enable_mkldnn=True,cpu_threads=30)

    save_folder = Output_path
    img_path = Img_path
    file_names = Barch_read(img_path)
    Failure_pictures = []
    for file in file_names:
        try:
            img = cv2.imread(file)
            result = table_engine(img)
            save_structure_res(result, save_folder,os.path.basename(file).split('.')[0])
            from PIL import Image
            # font_path = 'doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
            font_path = '/usr/share/fonts/dejavu/DejaVuSansCondensed.ttf' # PaddleOCR下提供字体包
            image = Image.open(file).convert('RGB')
            im_show = draw_structure_result(image, result,font_path=font_path)
            im_show = Image.fromarray(im_show)
            im_show.save(save_folder + '/'+os.path.basename(file).split('.')[0] + '/' + 'result.jpg')
        except Exception as e:
            print('\033[1;31m*****************************\033[0m')
            print(e)
            print('\033[1;31m*****************************\033[0m')
            Failure_pictures.append(str(img_path)+str(file))
            continue
    endtime = datetime.now()
    sleep(1)
    print('Running time: %s Seconds 转换失败%d次'%(endtime-starttime,len(Failure_pictures)))
    if(len(Failure_pictures)!=0):
        for i in Failure_pictures:
            print(i)

# Img_path= "./Out_images/"
# Output_path= "./PDF_output"
# ExtracttablefromPDF(Output_path,Img_path)