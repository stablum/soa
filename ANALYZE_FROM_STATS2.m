% IMPORT_FROM_STATS
% drag & drop stats. import as column vectors
%---------------------------------
% countsteps 
% expnum 
% meanedgesimportance
% stdedgesimportance
% numkills
% pathlength
% totalweight
%----------------------------------

% from columns to matrix using steps and expnum: rows=RUNS, columns=exp
% for each variable, take mean and 25/75%iles of each cycle
% make graphs var vs cycle
% make anova of [final] values
%----------------------------------
%% from columns to matrix using steps and expnum: rows=RUNS, columns=exp
expnum=expnum+1; % DO Once, better to FIX BEFORE
%% PUT everything under the correct policy structure.
%%%%%%%%%%%%%
npol=2%%%%%%%  CHANGE ME CAREFULLY: 1= pro_poor, 2=pro_rich, 3=pro_poor
%%%%%%%%%%%%%
%%
max_num_steps=max(countsteps);
max_num_exps=max(expnum);
steps=[1:max_num_steps];
exps=[1:max_num_exps];
ss=0;
pol(npol).all_p_l=[];pol(npol).all_std_imp=[];pol(npol).all_mean_imp=[];pol(npol).all_n_kill=[];pol(npol).all_tot_w=[];
for col= exps
    for row=steps
        ss=ss+1;
%         if mod(ss,max_num_steps+1)==0
%             ss=ss+1;
%         end
    if row==max_num_steps && col==max_num_exps
    else
            pol(npol).all_p_l(row,col)=pathlength(ss);
            pol(npol).all_std_imp(row,col)=stdedgesimportance(ss);
            pol(npol).all_mean_imp(row,col)=meanedgesimportance(ss);
            pol(npol).all_n_kill(row,col)=numkills(ss);
            pol(npol).all_tot_w(row,col)=totalweight(ss);
    end
    end
end
% p_l,std_imp,mean_imp,n_kill,tot_w
steps=1:max_num_steps-1;
pol(npol).all_p_l=pol(npol).all_p_l(steps,:); pol(npol).all_std_imp=pol(npol).all_std_imp(steps,:); pol(npol).all_mean_imp=pol(npol).all_mean_imp(steps,:);
pol(npol).all_n_kill=pol(npol).all_n_kill(steps,:); pol(npol).all_tot_w=pol(npol).all_tot_w(steps,:);
%% for each variable, take mean and 25/75%iles of each cycle

pol(npol).p_l.p25=prctile(pol(npol).all_p_l',25);    pol(npol).std_imp.p25=prctile(pol(npol).all_std_imp',25);    pol(npol).mean_imp.p25=prctile(pol(npol).all_mean_imp',25);  pol(npol).n_kill.p25=prctile(pol(npol).all_n_kill',25);  pol(npol).tot_w.p25=prctile(pol(npol).all_tot_w',25);       
pol(npol).p_l.p75=prctile(pol(npol).all_p_l',75);    pol(npol).std_imp.p75=prctile(pol(npol).all_std_imp',75);    pol(npol).mean_imp.p75=prctile(pol(npol).all_mean_imp',75);  pol(npol).n_kill.p75=prctile(pol(npol).all_n_kill',75);   pol(npol).tot_w.p75=prctile(pol(npol).all_tot_w',75);     
pol(npol).p_l.avg=mean(pol(npol).all_p_l');          pol(npol).std_imp.avg=mean(pol(npol).all_std_imp');             pol(npol).mean_imp.avg=mean(pol(npol).all_mean_imp');         pol(npol).n_kill.avg=mean(pol(npol).all_n_kill');          pol(npol).tot_w.avg=mean(pol(npol).all_tot_w');          

%% make graphs variable (mean,25 and 75 percentile) x cycle
npol=2
cols=[0,0,1; 1,0,0; 0,0,0];

figure(1);
p1=plot(steps,pol(npol).p_l.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).p_l.p25,'--','color',cols(npol,:)); hold on;
p3=plot(steps,pol(npol).p_l.p75,'--','color',cols(npol,:)); hold on;  
title('path length over cycles')
ylabel('path length'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure(2);
p1=plot(steps,pol(npol).std_imp.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).std_imp.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).std_imp.p75,'--','color',cols(npol,:)); hold on;  
title('stand deviation of the importance of the edges over the cycles');
ylabel('std dev of edge importance'); xlabel('cycles'); legend([p1,p2,p3],'mean','pile25','pile75')

figure(3);
p1=plot(steps,pol(npol).mean_imp.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).mean_imp.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).mean_imp.p75,'--','color',cols(npol,:)); hold on;  
title('mean edge importance over cycles')
ylabel('mean edge importance'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure(4);
p1=plot(steps,pol(npol).n_kill.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).n_kill.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).n_kill.p75,'--','color',cols(npol,:)); hold on;  
title('number of dead edges over cycles')
ylabel('number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure(5);
p1=plot(steps,pol(npol).tot_w.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).tot_w.p25,'--','color',cols(npol,:)); hold on;
p3=plot(steps,pol(npol).tot_w.p75,'--','color',cols(npol,:)); hold on;
title('total weight of the graph over cycles')
ylabel('total weight of the graph'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75');

%% make cumulative of killed edges x cycle

figure;
p1=plot(steps,cumsum(pol(npol).n_kill.avg),'color',cols(npol,:)); hold on;
p2=plot(steps,(pol(npol).n_kill.p25),'--','color',cols(npol,:)); hold on;
p3=plot(steps,cumsum(pol(npol).n_kill.p75),'--','color',cols(npol,:)); hold on;  
title('number of dead edges over cycles')
ylabel('number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')



%% a detailed graph

npol=2
cols=[0,0,1; 1,0,0; 0,0,0];

figure(1);
b1=plot(steps,pol(1).p_l.avg,'color',cols(1,:)); hold on;
b2=plot(steps,pol(1).p_l.p25,'--','color',cols(1,:)); hold on;
b3=plot(steps,pol(1).p_l.p75,'--','color',cols(1,:)); hold on; 

r1=plot(steps,pol(2).p_l.avg,'color',cols(2,:)); hold on;
r2=plot(steps,pol(2).p_l.p25,'--','color',cols(2,:)); hold on;
r3=plot(steps,pol(2).p_l.p75,'--','color',cols(2,:)); hold on; 
title('path length over cycles')
ylabel('path length'); xlabel('cycles');legend([b1,b2,b3],'mean','pile25','pile75');
legend([b1,r1],'pro poor','pro rich')

%% make anova of [final] values
countsteps

expnum

meanedgesimportance

stdedgesimportance

numkills

pathlength

totalweight