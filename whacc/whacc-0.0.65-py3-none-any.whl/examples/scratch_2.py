# # # # # # # # # import h5py
# # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # from whacc import image_tools
# # # # # # # # # import os
# # # # # # # # # from whacc import utils
# # # # # # # # #
# # # # # # # # # for h5_file in utils.get_h5s('/Users/phil/Dropbox/Autocurator/data/samsons_subsets/OLD_2'):
# # # # # # # # #     with h5py.File(h5_file, 'r') as h:
# # # # # # # # #         plt.figure(figsize=[20, 10])
# # # # # # # # #         plt.imshow(image_tools.img_unstacker(h['images'][:],40))
# # # # # # # # #         plt.title(h5_file.split('/')[-1])
# # # # # # # # #         plt.savefig(h5_file[:-3] + "_fig_plot.png")
# # # # # # # # #         plt.close()
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # for k in utils.get_h5s('/Users/phil/Dropbox/Autocurator/data/samsons_subsets/OLD_2'):
# # # # # # # # #     with h5py.File(k, 'r') as h:
# # # # # # # # #         k2 = k[:-3]+'_TMP.h5'
# # # # # # # # #         with h5py.File(k2, 'w') as h2:
# # # # # # # # #             h2.create_dataset('all_inds', data=h['all_inds'][50:])
# # # # # # # # #             h2.create_dataset('images', data=h['images'][50:])
# # # # # # # # #             h2.create_dataset('in_range', data=h['in_range'][50:])
# # # # # # # # #             h2.create_dataset('labels', data=h['labels'][50:])
# # # # # # # # #             h2.create_dataset('retrain_H5_info', data=h['retrain_H5_info'][:])
# # # # # # # # #     os.remove(k)
# # # # # # # # #     os.rename(k2, k)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # import h5py
# # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # from whacc import image_tools
# # # # # # # # #
# # # # # # # # # h5_file= '/Users/phil/Downloads/AH1159X18012021xS404_subset (1).h5'
# # # # # # # # # with h5py.File(h5_file, 'r') as h:
# # # # # # # # #     plt.figure(figsize=[20, 10])
# # # # # # # # #     plt.imshow(image_tools.img_unstacker(h['images'][:],10))
# # # # # # # # #     plt.title(h5_file.split('/')[-1])
# # # # # # # # #     print(len(h['labels'][:]))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # #
# # # # # # # # import numpy as np
# # # # # # # # import whacc
# # # # # # # # from whacc import analysis
# # # # # # # # import matplotlib.pyplot as plt
# # # # # # # #
# # # # # # # #
# # # # # # # # a = analysis.pole_plot(
# # # # # # # #     '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/master_train_test1.h5',
# # # # # # # #     pred_val = [0,0,0,0,0,0,0,.2,.4,.5,.6,.7,.8,.8,.6,.4,.2,.1,0,0,0,0],
# # # # # # # #     true_val = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
# # # # # # # #     len_plot = 10)
# # # # # # # #
# # # # # # # # a.plot_it()
# # # # # # # #
# # # # # # # #
# # # # # # # f1 = "/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/delete_after_oct_2021/AH0000x000000.h5"
# # # # # # # import h5py
# # # # # # #
# # # # # # # with h5py.File(f1, 'r') as h:
# # # # # # #     k = 'file_name_nums'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'full_file_names'
# # # # # # #     print(k, '   ', (h[k].shape))
# # # # # # #     k = 'images'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'in_range'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'labels'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'locations_x_y'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'max_val_stack'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'multiplier'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #     k = 'trial_nums_and_frame_nums'
# # # # # # #     print(k, '   ', h[k].shape)
# # # # # # #
# # # # # # # with h5py.File(save_directory + file_name, 'r+') as hf:  # with -> auto close in case of failure
# # # # # # #     hf.create_dataset("asdfasdf", data=loc_stack_all2)
# # # # # # #     for i, k in enumerate(loc_stack_all):
# # # # # # #         print(i)
# # # # # # #         hf.create_dataset("aaa"+str(i), data=k)
# # # # # # #
# # # # # # # loc_stack_all2 = loc_stack_all.copy()
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # for i, k in enumerate(loc_stack_all):
# # # # # # #     if not k.shape==(4000, 2):
# # # # # # #         print(i)
# # # # # # #     # for kk in k.flatten():
# # # # # # #     #     print(kk.shape)
# # # # # # #     #         # if not kk.dtype=='int64':
# # # # # # #     #         #     print('booooo')
# # # # # # #     #
# # # # # # #     #
# # # # # #
# # # # # #
# # # # # # # import h5py
# # # # # # # import numpy as np
# # # # # # # import matplotlib.pyplot as plt
# # # # # # # cnt = 0
# # # # # # # f = "/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000.h5"
# # # # # # # with h5py.File(f, 'r') as h:
# # # # # # #     print(len(h['labels']))
# # # # # # #     for k in range(0, 1163998, 20000):
# # # # # # #         plt.figure()
# # # # # # #         plt.imshow(h['images'][k])
# # # # # # #         cnt+=1
# # # # # # #         # if cnt>=20 :
# # # # # # #         #     asdfasdf
# # # # # #
# # # # # # from whacc import utils
# # # # # # from whacc import image_tools
# # # # # # import copy
# # # # # # import h5py
# # # # # # f = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000.h5'
# # # # # # f2 = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_80border_single_frame.h5'
# # # # # #
# # # # # # h5c = image_tools.h5_iterative_creator(f2,
# # # # # #                  overwrite_if_file_exists=False,
# # # # # #                  max_img_height=61,
# # # # # #                  max_img_width=61,
# # # # # #                  close_and_open_on_each_iteration=True,
# # # # # #                  color_channel=False)
# # # # # # with h5py.File(f, 'r') as h:
# # # # # #     print(len(h['labels'][:]))
# # # # # #     h_cont = copy.deepcopy(h['labels'][:])
# # # # # # utils.create_master_dataset(h5c, [f], [h_cont], borders=80, max_pack_val=100)
# # # # # #
# # # # # #
# # # # # # ####
# # # # # #
# # # # # #
# # # # # # f = "/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_80border_single_frame.h5"
# # # # # # with h5py.File(f, 'r') as h:
# # # # # #     utils.print_list_with_inds(h.keys())
# # # # # #     tmp1 = copy.deepcopy(h['frame_nums'][:])
# # # # # #
# # # # # #
# # # # # # """
# # # # # # add teh frame and trail number to add teh frame num info to each with the same name!!!!
# # # # # # """
# # # # # #
# # # # # # h5file = "/Users/phil/Downloads/untitled folder 2/AH0000x000000_small_tester.h5"
# # # # # # def make_sure_frame_nums_exist(h5file):
# # # # # #     with h5py.File(h5file, 'r+') as h:
# # # # # #         key_list = list(h.keys())
# # # # # #         if 'frame_nums' in key_list:
# # # # # #             print("""'frame_nums' already in the key list""")
# # # # # #             return None
# # # # # #         assert 'trial_nums_and_frame_nums' in key_list, """key 'trial_nums_and_frame_nums' must be in the provided h5 this is the only reason program exists"""
# # # # # #         frame_nums = h['trial_nums_and_frame_nums'][1, :]
# # # # # #         h.create_dataset('frame_nums', shape=np.shape(frame_nums), data=frame_nums)
# # # # # # make_sure_frame_nums_exist(h5file)
# # # # # #
# # # # # # frame_num_array_list = get_h5_key_and_dont_concatenate(h5_to_split_list, key_name='trial_nums_and_frame_nums')
# # # # # # frame_num_array_list = list(frame_num_array_list[0][-1])
# # # # # # frame_num_array_list = [frame_num_array_list]
# # # # # # bd = '/Users/phil/Downloads/untitled folder 2/'
# # # # # # split_h5_loop_segments(h5_to_split_list, [1, 3], [bd+'TRASH', bd+'TRASH2'], frame_num_array_list, chunk_size=10000, add_numbers_to_name=False,
# # # # # #              disable_TQDM=False, set_seed = None)
# # # # # #
# # # # # #
# # # # # # h5file = '/Users/phil/Downloads/untitled folder 2/TRASH2.h5'
# # # # # # utils.print_h5_keys(h5file)
# # # # # # with h5py.File(h5file, 'r') as h:
# # # # # #     print(len(h['labels'][:]))
# # # # # #     print(h['frame_nums'][:])
# # # # # #
# # # # #
# # # # #
# # # # from whacc import image_tools, utils
# # # # h5_to_split_list = "/Users/phil/Downloads/untitled folder 2/AH0000x000000_small_tester.h5"
# # # # h5_to_split_list = [h5_to_split_list]
# # # # utils.print_h5_keys(h5_to_split_list[0])
# # # # bd = '/Users/phil/Downloads/untitled folder 2/'
# # # # image_tools.split_h5_loop_segments(h5_to_split_list, [1, 3], [bd+'TRASH', bd+'TRASH2'], chunk_size=10000, add_numbers_to_name=False,
# # # #              disable_TQDM=False, set_seed = None)
# # # #
# # # #
# # # # from whacc import utils
# # # # from whacc import image_tools
# # # # from keras.preprocessing.image import ImageDataGenerator
# # # # import h5py
# # # # import matplotlib.pyplot as plt
# # # # from tqdm import tqdm
# # # # from imgaug import augmenters as iaa  # optional program to further augment data
# # # # h5_subset_file = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/for_aug/3lag/AH0000x000000_5border_single_frame_onset_offset_for_aug_3lag_remove_2_edges.h5'
# # # # for h5_subset_file in utils.get_files('/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/for_aug/', '*remove_2_edges.h5'):
# # # #     datagen = ImageDataGenerator(rotation_range=360,  #
# # # #                                  width_shift_range=.1,  #
# # # #                                  height_shift_range=.1,  #
# # # #                                  shear_range=.00,  #
# # # #                                  zoom_range=.25,
# # # #                                  brightness_range=[0.2, 1.2])  #
# # # #
# # # #     with h5py.File(h5_subset_file, 'r') as hf:
# # # #         test_img = hf['images'][2]  # grab a single image
# # # #     num_aug = 20
# # # #
# # # #     aug_ims, _ = image_tools.augment_helper(datagen, num_aug, 0 ,test_img, -1)  # make 99 of the augmented images and output 1 of th original
# # # #     # '-1' is the label associate ith the image, we dont care becasue we just want the iamge so it doenst matter what it is here
# # # #
# # # #     # plt.figure(figsize=[5, 5])
# # # #     # plt.imshow(image_tools.img_unstacker(aug_ims, 10), )
# # # #     # plt.show()
# # # #
# # # #     gaussian_noise = iaa.AdditiveGaussianNoise(loc = 0, scale=3)
# # # #     aug_ims_2 = gaussian_noise.augment_images(aug_ims)
# # # #     # plt.figure(figsize=[10, 10])
# # # #     # plt.imshow(image_tools.img_unstacker(aug_ims_2, 10))
# # # #     # plt.show()
# # # #
# # # #     num_aug = 1
# # # #     for ii in range(10):
# # # #         # once we are happy with our augmentation process we can make an augmented H5 file using class
# # # #         new_H5_file = h5_subset_file.split('.')[0] + '_AUG_' + str(ii) + '.h5' # create new file name based on teh original H5 name
# # # #         h5creator = image_tools.h5_iterative_creator(new_H5_file, overwrite_if_file_exists=True,
# # # #                                                      close_and_open_on_each_iteration=True, color_channel=True)
# # # #         utils.get_class_info(h5creator)
# # # #         with h5py.File(h5_subset_file, 'r') as hf:
# # # #             for image, label in zip(tqdm(hf['images'][:]), hf['labels'][:]):
# # # #                 aug_img_stack, labels_stack = image_tools.augment_helper(datagen, num_aug, 0, image, label)
# # # #                 aug_img_stack = gaussian_noise.augment_images(aug_img_stack) # optional
# # # #                 h5creator.add_to_h5(aug_img_stack[:, :, :, :], labels_stack)
# # # #
# # # #
# # # #
# # # #
# # # # h5 = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_0.h5'
# # # # a = analysis.pole_plot(h5)
# # # # a.next()
# # # # h5 = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_1.h5'
# # # # b = analysis.pole_plot(h5)
# # # # b.next()
# # # #
# # # #
# # # #
# # # # from whacc import utils
# # # # all_h5s = utils.get_h5s('/Users/phil/Dropbox/HIRES_LAB/curation_for_auto_curator/finished_contacts/')
# # # # all_h5s_imgs = utils.get_h5s('/Users/phil/Dropbox/HIRES_LAB/curation_for_auto_curator/H5_data/')
# # # # h_cont = utils._get_human_contacts_(all_h5s)
# # # # h5c = image_tools.h5_iterative_creator('/Users/phil/Dropbox/HIRES_LAB/curation_for_auto_curator/holy_set_80_border_single_frame.h5',
# # # #                                        overwrite_if_file_exists = True,
# # # #                                        color_channel = False)
# # # # utils.create_master_dataset(h5c, all_h5s_imgs, h_cont, borders = 80, max_pack_val = 100)
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # #
# # # # # from whacc import image_tools
# # # # #
# # # # # # bd = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border/'
# # # # # # h5_to_split_list = ['/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_80border_single_frame.h5']
# # # # # # image_tools.split_h5_loop_segments(h5_to_split_list, [7, 3], [bd+'train', bd+'val'], chunk_size=1000, add_numbers_to_name=False,
# # # # # #              disable_TQDM=False, set_seed = 0, color_channel=False)
# # # # # #
# # # # #
# # # # #
# # # # # bd = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border_aug_0_to_9_test/'
# # # # # h5_to_split_list = ['/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoC2uratorDiverseDataset/AH0000x000000/AH0000x000000_80border_single_frame.h5',
# # # # #                     '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_9.h5']
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_8.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_7.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_6.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_5.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_4.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_3.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_2.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_1.h5',
# # # # #                     # '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_3border_single_frame_onset_offset_for_aug_AUG_0.h5',]
# # # # # image_tools.split_h5_loop_segments(h5_to_split_list, [1, 1, 1, 99], [bd+'train1',bd+'train2',bd+'train3', bd+'val4'], chunk_size=1000, add_numbers_to_name=False,
# # # # #              disable_TQDM=False, set_seed = 0, color_channel=False)
# # # # #
# # # # #
# # # # # import h5py
# # # # # with h5py.File(bd+'train1.h5', 'r') as h:
# # # # #     print(h['images'][:].shape)
# # # # #     print(h['labels'][:].shape)
# # # # #     print(sum(h['frame_nums'][:]))
# # # # #
# # # # #
# # # # #
# # # # #
# # # #
# # # #
# # # # from whacc import utils
# # # # x = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border_aug_0_to_9/data/ALT_LABELS/train_regular_ALT_LABELS.h5'
# # # # keys = utils.print_h5_keys(x, return_list=True)
# # # # tmp1 = []
# # # # for k in keys:
# # # #     tmp1.append(image_tools.get_h5_key_and_concatenate([x], k))
# # # #
# # # # for k in tmp1:
# # # #     print(list(set(k)))
# # # #
# # # #
# # # # x = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border_aug_0_to_9/data/regular/val_regular.h5'
# # # # x = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/for_aug/3lag_diff/AH0000x000000_5border_single_frame_onset_offset_for_aug_3lag_diff_remove_2_edges_AUG_5.h5'
# # # # x = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/for_aug/3lag_diff/train.h5'
# # # # x = l1[0]
# # # # x = l2[0]
# # # # x = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border_aug_0_to_9/data/regular/val_regular.h5'
# # # # a = image_tools.get_h5_key_and_concatenate([x])
# # # # print(list(set(a)))
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # def label_naming_shorthand_dict(name_key=None):
# # # #     label_naming_shorthand_dict = {
# # # #         '[0, 1, 2, 3, 4, 5]- (no touch, touch, onset, one after onset, offset, one after offset)': 'on-off_set_and_one_after',
# # # #         '[0, 1, 2, 3]- (no touch, touch, onset, offset': 'on-off_set',
# # # #         '[0, 1, 2]- (no event, onset, offset)': 'only_on-off_set',
# # # #         '[0, 1]- (no touch, touch)': 'regular',
# # # #         '[0, 1]- (not offset, offset)': 'only_offset',
# # # #         '[0, 1]- (not onset, onset)': 'only_onset',
# # # #         '[0, 1, 2, 3]- (no touch, touch, one after onset, offset)': 'overlap_whisker_on-off'}
# # # #     if name_key is None:
# # # #         return label_naming_shorthand_dict
# # # #     else:
# # # #         return label_naming_shorthand_dict[name_key]
# # # #
# # # # def copy_over_new_labels(label_key_name, image_h5_list, label_h5_list):
# # # #     label_key_shorthand = label_naming_shorthand_dict(label_key_name)
# # # #     for img_src, lab_src in zip(image_h5_list, label_h5_list):
# # # #         utils.copy_h5_key_to_another_h5(lab_src, img_src, label_key_name, 'labels')
# # # #
# # # # from whacc import image_tools
# # # # from whacc import utils
# # # # from whacc import analysis
# # # # import matplotlib.pyplot as plt
# # # #
# # # # x = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/small_h5s/data/3lag/small_train_3lag.h5'
# # # #
# # # # alt_labels = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/small_h5s/data/ALT_LABELS/small_train_ALT_LABELS.h5'
# # # #
# # # # copy_over_new_labels('[0, 1, 2, 3]- (no touch, touch, one after onset, offset)', [x], [alt_labels])
# # # #
# # # # a = analysis.pole_plot(x)
# # # # a.len_plot = 11
# # # # a.current_frame = 36
# # # # a.plot_it()
# # # # plt.ylim([-.5, 6])
# # #
# # # def search_sequence_numpy(arr, seq, return_type='indices'):
# # #     Na, Nseq = arr.size, seq.size
# # #     r_seq = np.arange(Nseq)
# # #     M = (arr[np.arange(Na - Nseq + 1)[:, None] + r_seq] == seq).all(1)
# # #
# # #     if return_type == 'indices':
# # #         return np.where(M)[0]
# # #     elif return_type == 'bool':
# # #         return M
# # #
# # #
# # # import numpy as np
# # #
# # # a = np.asarray([0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1])
# # # a = np.asarray([0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1])
# # #
# # # a1 = search_sequence_numpy(a, np.asarray([0, 0, 1, 0, 0]))
# # # a2 = search_sequence_numpy(a, np.asarray([1, 1, 0, 1, 1]))
# # #
# # # print(a1, a2)
# # #
# # # np.convolve(a, np.ones(4) / 4)
# # #
# # # x = np.asarray([0, 1, 0])
# # # seg_len = len(x)
# # # border = x[0]
# # # for k in a1:
# # #     k = int(k + np.floor(seg_len / 2))
# # #     side_sums = 0
# # #     for kk in range(2, 10):
# # #         side_sums = a[k - kk] + a[k + kk] + side_sums
# # #         print(side_sums / ((kk - 1) * 2))
# # #         asdf
# # #
# # #     sdfadf
#
# # from whacc import analysis
# # pp = analysis.pole_plot('/Users/phil/Dropbox/Colab data/H5_data/OG/AH0407_160613_JC1003_AAAC-006.h5')
# # pp.plot_it()
# # pp.current_frame=8271
# #
# #
# #
# # from whacc import utils
# # x  = utils.print_h5_keys('/Users/phil/Dropbox/Colab data/H5_data/ALT_LABELS_FINAL_PRED/AH0407_160613_JC1003_AAAC_ALT_LABELS.h5', True, False)
# # tmp1 = utils.lister_it(x, keep_strings = ['MODEL_2_'])
# # print(len(tmp1))
#
#
# from google.colab import drive
# import numpy as np
# import h5py
# import os
# from whacc import utils
#
# drive.mount('/content/gdrive')
#
# base_dir = '/content/gdrive/My Drive/Colab data/curation_for_auto_curator/H5_data/'
# h5_list_to_write = utils.get_h5s(base_dir)
# all_h5s = utils.get_h5s('/content/gdrive/My Drive/Colab data/curation_for_auto_curator/finished_contacts/',
#                         print_h5_list=False)
# h_cont, h_names = utils._get_human_contacts_(all_h5s)
# print('--------\npercent fully agree\n--------')
# for k in h_cont:
#     a = np.mean(np.mean(k, axis=0) == 1)
#     b = np.mean(np.mean(k, axis=0) == 0)
#     print(np.round(a + b, 4))
#
#
# def add_to_h5(h5_file, key, values, overwrite_if_exists=False):
#     all_keys = utils.print_h5_keys(h5_file, return_list=True, do_print=False)
#     with h5py.File(h5_file, 'r+') as h:
#         if key in all_keys and overwrite_if_exists:
#             print('key already exists, overwriting value...')
#             del h[key]
#             h.create_dataset(key, data=values)
#         elif key in all_keys and not overwrite_if_exists:
#             print("""key already exists, NOT overwriting value..., \nset 'overwrite_if_exists' to True to overwrite""")
#         else:
#             h.create_dataset(key, data=values)
#
#
# for kk, h5 in zip(h_cont, all_h5s):
#     F_NAME = os.path.basename(h5).split('Phil_')[-1][:-3]
#     h52write = utils.lister_it(h5_list_to_write, keep_strings=F_NAME)[0]
#     print(h52write)
#
#     avg_cont = (np.mean(kk, axis=0) > .5) * 1
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([0, 1, 0]))
#     for k in tmp1 + 1:
#         avg_cont[k] = 0
#
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([1, 0, 1]))
#     for k in tmp1 + 1:
#         avg_cont[k] = 1
#
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([0, 1, 1, 0]))
#     for k in tmp1 + 1:
#         avg_cont[k] = 0
#     for k in tmp1 + 2:
#         avg_cont[k] = 0
#
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([1, 0, 0, 1]))
#     for k in tmp1 + 1:
#         avg_cont[k] = 1
#     for k in tmp1 + 2:
#         avg_cont[k] = 1
#
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([0, 1, 0]))
#     assert tmp1.size == 0
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([1, 0, 1]))
#     assert tmp1.size == 0
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([0, 1, 1, 0]))
#     assert tmp1.size == 0
#     tmp1 = search_sequence_numpy(avg_cont, np.asarray([1, 0, 0, 1]))
#     assert tmp1.size == 0
#
#     utils.add_to_h5(h52write, 'labels', avg_cont, overwrite_if_exists=True)
#
# utils.make_alt_labels_h5s(base_dir)
# alt_label_dir = '/content/gdrive/My Drive/Colab data/curation_for_auto_curator/ALT_LABELS/'
#
# to_pred_h5s = '/content/gdrive/My Drive/colab_data2/model_testing/all_data/final_predictions/ALT_LABELS_FINAL_PRED'
# to_pred_h5s = utils.get_h5s(to_pred_h5s)
#
# tmp1 = utils.get_h5s(alt_label_dir)
# utils.print_h5_keys(tmp1[0])
# for h5, h5_dest in zip(tmp1, to_pred_h5s):
#     assert os.path.basename(h5) == os.path.basename(h5_dest)
#     keys = utils.print_h5_keys(h5, return_list=True, do_print=False)
#     for key in keys:
#         utils.copy_h5_key_to_another_h5(h5, h5_dest, key)
#
#
#
# import numpy as np
# import h5py
# import os
# from whacc import utils, image_tools
# import matplotlib.pyplot as plt
#
# tmp1 = "/Users/phil/Dropbox/Colab data/H5_data/ALT_LABELS_FINAL_PRED/AH0705_171105_PM0175_AAAB_ALT_LABELS.h5"
# a = utils.print_h5_keys(tmp1, 1, 1)
# b = image_tools.get_h5_key_and_concatenate([tmp1], a[34])
# plt.plot(b[:16000])
#
#
#
#
#
xxx = ['/content/data_AH0407_160613_JC1003_AAAC/3lag/train_3lag_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/single_frame/train.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/val_3lag_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/val_3lag_diff_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/val_3lag_AUG_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/train_3lag_diff_AUG_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/train_regular.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/single_frame/val.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/train_3lag_diff_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/train_3lag_diff.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/val_regular.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/train_3lag.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/ALT_LABELS/train_ALT_LABELS.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/val_3lag.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/single_frame/train_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/val_regular_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/val_3lag_diff.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/train_regular_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/ALT_LABELS/val_ALT_LABELS.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/train_3lag_AUG_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/val_3lag_diff_AUG_AUG.h5.h5']


import numpy as np

# utils.lister_it(xxx, remove_string=['ALT_LABELS', 'single_frame'])
def lister_it(in_list, keep_strings='', remove_string=None):
    def index_list_of_strings(in_list2, cmp_string):
        return np.asarray([cmp_string in string for string in in_list2])

    if isinstance(keep_strings, str): keep_strings = [keep_strings]
    if isinstance(remove_string, str): remove_string = [remove_string]

    keep_i = np.asarray([False]*len(in_list))
    for k in keep_strings:
        keep_i = np.vstack((keep_i, index_list_of_strings(in_list, k)))
    keep_i = np.sum(keep_i, axis = 0)>0

    remove_i = np.asarray([True]*len(in_list))
    if remove_string is not None:
        for k in remove_string:
            remove_i = np.vstack((remove_i, np.invert(index_list_of_strings(in_list, k))))
        remove_i = np.product(remove_i, axis = 0)>0

    inds = keep_i * remove_i#np.invert(remove_i)
    out = np.asarray(in_list)[inds]
    return out

xxx = ['123', '234', '345', '456', '567', '678']
tmp1 = lister_it(xxx, keep_strings=['1', '2', '6'], remove_string=['4'])
# tmp1 = lister_it(xxx, keep_strings=['1', '2', '6'], remove_string=['4', '5'])
# tmp1 = lister_it(xxx, keep_strings=['1', '2', '6'], remove_string=None)
tmp1 = lister_it(xxx, keep_strings='', remove_string='4')
tmp1



substring_in_list
def edit_list_of_strings(list_of_strings, edit_type, edit_string):
    if edit_type not in ['keep', 'remove']:
        assert False, """edit_type needs to be with 'keep' OR 'remove'"""
    x = []
    for k in list_of_strings:
        if edit_string in k:
            x.append(1)
        else
            x.append(0)



def lister_it(in_list, keep_strings=None, remove_string=None):

    if isinstance(keep_strings, str):
        keep_strings = [keep_strings]
    if isinstance(remove_string, str):
        remove_string = [remove_string]

    if keep_strings is None:
        new_list = copy.deepcopy(in_list)
    else:
        new_list = []
        for L in in_list:
            for k in keep_strings:
                if k in L:
                    new_list.append(L)

    if remove_string is None:
        new_list_2 = copy.deepcopy(in_list)
    else:
        new_list_2 = []
        for L in new_list:
            for k in remove_string:
                if k not in L:
                    new_list_2.append(L)
    final_list = intersect_lists([new_list_2, new_list])
    return final_list

from whacc import utils
xxx = ['/content/data_AH0407_160613_JC1003_AAAC/3lag/train_3lag_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/single_frame/train.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/val_3lag_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/val_3lag_diff_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/val_3lag_AUG_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/train_3lag_diff_AUG_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/train_regular.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/single_frame/val.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/train_3lag_diff_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/train_3lag_diff.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/val_regular.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/train_3lag.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/ALT_LABELS/train_ALT_LABELS.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/val_3lag.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/single_frame/train_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/val_regular_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/val_3lag_diff.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/regular/train_regular_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/ALT_LABELS/val_ALT_LABELS.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag/train_3lag_AUG_AUG.h5.h5',
 '/content/data_AH0407_160613_JC1003_AAAC/3lag_diff/val_3lag_diff_AUG_AUG.h5.h5']

utils.lister_it(xxx, remove_string=['ALT_LABELS', 'single_frame'])
