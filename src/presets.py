# select some repsentative data 
# following the presets we are going to use
preset_dict = {
    'mul_vegetation': {'width':325,'channel_count':8,'channels':[7,5,3],'subfolder':'MUL'},
    'mul_urban': {'width':325,'channel_count':8,'channels':[8,7,5],'subfolder':'MUL'},     
    'mul_blackwater': {'width':325,'channel_count':8,'channels':[7,8,1],'subfolder':'MUL'},     
    'mul_ir1': {'width':325,'channel_count':8,'channels':[7,7,7],'subfolder':'MUL'}, 
    'mul_ir2': {'width':325,'channel_count':8,'channels':[8,8,8],'subfolder':'MUL'},      
    'pan': {'width':1300,'channel_count':1,'channels':[1],'subfolder':'PAN'},
    'rgb_ps': {'width':1300,'channel_count':3,'channels':[1,2,3],'subfolder':'RGB-PanSharpen'},
    'mul_ps_vegetation': {'width':1300,'channel_count':8,'channels':[7,5,3],'subfolder':'MUL-PanSharpen'},
    'mul_ps_urban': {'width':1300,'channel_count':8,'channels':[8,7,5],'subfolder':'MUL-PanSharpen'},     
    'mul_ps_blackwater': {'width':1300,'channel_count':8,'channels':[7,8,1],'subfolder':'MUL-PanSharpen'},     
    'mul_ps_ir1': {'width':1300,'channel_count':8,'channels':[7,7,7],'subfolder':'MUL-PanSharpen'}, 
    'mul_ps_ir2': {'width':1300,'channel_count':8,'channels':[8,8,8],'subfolder':'MUL-PanSharpen'},        
}